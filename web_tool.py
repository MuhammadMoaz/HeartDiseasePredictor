from flask import Flask, render_template, request
import pandas as pd
from main import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bmi', methods=['POST'])
def calc_bmi():
    weight = float(request.form['Weight'])
    height = float(request.form['Height'])

    bmi = weight / (height ** 2)
    
    return render_template('index.html', bmi=f"BMI: {bmi}")

@app.route('/predict', methods=['POST'])
def predict():

    sex_dict = {
        'Male': 1,
        'Female': 0
    }

    cp_dict = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non--Anginal Pain": 2,
        "Asymptotic" : 3
    }    
        
    fbs_dict = {
        "Yes": 1,
        "No": 0
    }

    restecg_dict = {
        "Normal": 0,
        "Having ST-T wave abnormality": 1,
        "left ventricular hyperthrophy" : 2
    }

    exang_dict = {
        "Yes": 1,
        "No": 0
    }

    slope_dict = {
        "Upsloping": 0,
        "Flat": 1,
        "Downsloping": 2
    }

    thal_dict = {
        "Normal": 1,
        "Fixed Defect": 2,
        "Reversible Defect": 3
    }

    # Get Values
    age = request.form['age']
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']
    

    sex = sex_dict[sex]
    cp = cp_dict[cp]
    fbs = fbs_dict[fbs]
    restecg = restecg_dict[restecg]
    exang = exang_dict[exang]
    slope = slope_dict[slope]
    thal = thal_dict[thal]
    
    patient_info = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    prediction =  best_model.predict([patient_info])

    if prediction == [0]:
        prediction = "low chance of heart diseas"
    else:
        prediction = "high chance of heart disease"

    return render_template('index.html', prediction=prediction)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# PDA
# - Age
# - Gender
# - Exercise Habits
# - Smoking
# - Family Heart Disease
# - Diabetes
# - BMI
# - High Blood Pressure [Optional]
# - Alcohol Consumption lmh
# - Stress Level lmh
# - Sleep Hours 
# - Sugar Consumption lmh