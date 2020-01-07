import numpy as np
import pandas as pd
import re
import keras
import pickle
import librosa
from keras.models import load_model

def model_load_compile():
    with open('./labels', 'rb') as f:
        lb = pickle.load(f)
        print('labels loaded')

    # loading keras model (arhitecture, weights and compiler)
    model = load_model('./my_sentimental_model.h5')
    model._make_predict_function() #keras is not thread safe: keras_model._make_predict_function() check my StackOverflow on it:
    # https://stackoverflow.com/questions/53391618/tensor-tensorpredictions-softmax0-shape-1000-dtype-float32-is-not-an/59238039#59238039
    print('model loaded')
    return model, lb

def data_mfcc(file_address):
    # Lets transform the dataset so we can apply the predictions
    X, sample_rate = librosa.load(file_address
                              ,res_type='kaiser_fast'
                              ,duration=2.5
                              ,sr=44100
                              ,offset=0.5
                             )

    sample_rate = np.array(sample_rate)
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
    newdf = pd.DataFrame(data=mfccs).T
    print(f' Transformed data: \n {newdf}')
    newdf = np.expand_dims(newdf, axis=2)
    print ('mfcc done')
    return newdf

def predict_func(model, lb, newdf):
    # predict
    newpred = model.predict(newdf, batch_size=16, verbose=1)
    print(newpred)
    # Get the final predicted label
    final = newpred.argmax(axis=1)
    final = final.astype(int).flatten()
    prediction_result = (lb.inverse_transform((final)))
    print(prediction_result) 

    return prediction_result

def arrange_predictions(prediction_result):
    pr = np.array_str(prediction_result)
    part = re.split('\W+|_', pr)
    pred_text = 'What a lovely ' + part[1] + ' voice you have. You sound: '+ part[2]+'.'
    print(pred_text)
    return pred_text
