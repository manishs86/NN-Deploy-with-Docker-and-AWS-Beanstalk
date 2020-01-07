from flask import Flask, request, render_template

import os
from glob import glob
import pandas as pd
import numpy as np
from werkzeug import secure_filename
from commons import data_mfcc
from commons import predict_func
from commons import model_load_compile
from commons import arrange_predictions

application = Flask(__name__)

model, lb = model_load_compile()

temp_last_filename = ""

@application.route('/')
def index():
        return render_template('index.html')

@application.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            application.logger.debug("[server] no file part")
            return '[server] no file part'

        f = request.files['file']

        if f.filename == '':
            application.logger.debug("[server] empty file")
            return '[server] empty file'

        filename = secure_filename(f.filename)

        global temp_last_filename
        temp_last_filename = filename
        print(f"numele creat este: {temp_last_filename}")

        f.save(os.path.join(application.root_path,'uploads', filename))

        application.logger.debug("[server] file uploaded")
        return '[server] file uploaded'

@application.route('/predict', methods=['GET', 'POST'])
def predict_button():
    if request.method == 'POST':
        application.logger.debug("[server] predict sentiment")
        #get file name
        filename = './uploads/' + temp_last_filename
        print(f"adresa citita este: {filename}")
        #Take the file name and load it into python for mfcc and prediction
        newdf = data_mfcc(filename)  # MFCC The Newest File
        pred_res = predict_func(model, lb, newdf)
        pred_text = arrange_predictions(pred_res)
        #return the results
    return render_template('index.html', message=pred_text)

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
