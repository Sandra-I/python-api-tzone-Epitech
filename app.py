from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
import base64
from PIL import Image
import io
from werkzeug.utils import secure_filename
from imgToText import process_image
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/upload', methods=['POST']) 
def upload_base64_file(): 
    """ 
        Upload image with base64 format and get car make model and year 
        response 
    """

    data = request.args.get('img')
    # print(data)
    image = base64.b64decode(str(data))       
    fileName = 'test.png'
    imagePath = ('C:/Users/rkane/OneDrive/Bureau/TZone_python/'+"test.png")
    img = Image.open(io.BytesIO(image))
    img.save(imagePath, 'png')
    process_image(imagePath)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = int(8080))
