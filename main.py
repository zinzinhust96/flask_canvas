import os

import cv2
from flask import Flask, redirect, render_template, request, send_file, url_for

app = Flask(__name__)

UPLOAD_FOLDER = './upload'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/post_image', methods=['POST'])
def post_image():
    if 'file' not in request.files:
        print("No file")
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return redirect(request.url)
    if file:
        saved_path = os.path.join(UPLOAD_FOLDER, file.filename)     
        file.save(saved_path)
        print('saving files ...')
        
        return redirect(url_for('show_image', saved_name=file.filename))

    return None

@app.route('/show_image/<string:saved_name>', methods=['GET'])
def show_image(saved_name):
    return render_template('frame.html', frame=saved_name)

@app.route('/frame/<string:saved_name>', methods=['GET'])
def image(saved_name):
    saved_path = os.path.join(UPLOAD_FOLDER, saved_name)
    return send_file(saved_path, as_attachment=False)

if __name__ == '__main__':
    app.run(host='localhost', port=4321)
