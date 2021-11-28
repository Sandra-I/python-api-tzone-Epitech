from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
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
    return 'Well pinging!'
 
@app.route('/upload', methods=['POST']) 
def upload_base64_file(): 
    """ 
        Upload image with base64 format and get car make model and year 
        response 
    """
    data = request.get_json()
    data = data['img']    
    image = base64.b64decode(data)       
    imagePath = ('./static/uploads/test.png')
    img = Image.open(io.BytesIO(image))
    img.save(imagePath)
    textToReturn = process_image(imagePath)
    return jsonify({ 'text': textToReturn })
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = int(8080))
