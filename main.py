from flask import Flask
from flask import render_template
from flask import request

import pandas as pd
import pickle

from Forms import PredictForm
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/',  methods=['GET', 'POST'])
def home():
    form = PredictForm()

    return render_template('index.html', form=form)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    model = load_model()
    rm = float(request.form['rm'])
    lstat = float(request.form['lstat'])
    ptratio = float(request.form['ptratio'])

    d = {'RM': [rm], 'LSTAT': [lstat], 'PTRATIO': [ptratio]}
    res = pd.DataFrame(data=d)


    prediction = model.predict(res)

    return render_template('predict.html', prediction=prediction[0])


def load_model():

    # Load the saved model
    with open('model/model_boston_housing_v1.pkl', 'rb') as file:
        model = pickle.load(file)

    return model
