import re
import cv2
import pytesseract
import numpy as np
from PIL import Image

def extract_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Image not found!"
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((2, 2), np.uint8)
    gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    custom_config = r'--oem 3 --psm 6'
    extracted_text = pytesseract.image_to_string(gray, config = custom_config)

    pattern = r'[A-Z]\d{7}'
    matches = re.findall(pattern, extracted_text)
    
    serial_number = matches[0] if matches else "No Serial Number Found!"
    
    return serial_number
