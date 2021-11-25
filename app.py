from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import urllib.request
import os
import base64
from PIL import Image
import io
from werkzeug.utils import secure_filename
from imgToText import process_image
from translation import translation_text
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

class InvalidUsage(Exception):
    status_code = 400
    print('here')
    def __init__(self, message, status_code=None, payload=None):
        print('init')
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
    
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

@app.route('/upload-with-translation', methods=['POST'])
def upload_with_translation():
    request_data = request.get_json()
    text_to_translate = None
    imagePath = None
    if request_data:
        if 'img' in request_data:
            data = request_data['img']
            target_lang = request_data['language']
            image = base64.b64decode(data)       
            imagePath = ('./static/uploads/imagetest.png')
            img = Image.open(io.BytesIO(image))
            img.save(imagePath)
            text_to_translate = process_image(imagePath)

            try:
                translation_result = translation_text(text_to_translate, target_lang)
                translated_text = translation_result.text
                original_lang = translation_result.detected_source_lang
                print(translation_text)
                return jsonify({
                    'original': { 'lang': original_lang, 'text': text_to_translate },
                    'translated': { 'lang': target_lang, 'text': translated_text }
                })
            except Exception as e:
                raise InvalidUsage(str(e))
            finally:
                os.remove(imagePath)

 
if __name__ == "__main__":
    app.run(host="0.0.0.0",port = int(8080))
