from quart import Quart, render_template, request
import os
from ocr import extract_text

app = Quart(__name__)
UPLOAD_FOLDER = 'static/uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ['GET', 'POST'])
async def index():
    serial_number = None
    image_path = None 

    if request.method == 'POST':
        form = await request.form 
        files = await request.files 
        file = files['image']
        
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            await file.save(filepath)
            image_path = filepath
            serial_number = extract_text(filepath)

    return await render_template('index.html', serial_number = serial_number, image_path = image_path)
    
if __name__ == '__main__':
    app.run(debug = True)
