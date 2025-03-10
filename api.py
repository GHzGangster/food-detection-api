import os
import time

from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename

from common import input_dir_path, output_dir_path, predict

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = input_dir_path

CORS(app)

@app.route('/predict', methods=['POST'])
def handle_predict():
    upload_path = app.config['UPLOAD_FOLDER']
    if upload_path is None:
        return "Bad upload path", 400

    if 'file' not in request.files:
        return "Missing file", 400

    file = request.files['file']

    t = int(time.time())

    input_path = os.path.join(upload_path, "{}-{}".format(t, secure_filename(file.filename)))

    file.save(input_path)

    output_path = os.path.join(output_dir_path, "{}.png".format(t))

    if not predict(input_path, output_path):
        return "Prediction failed", 400

    return send_file(output_path)
