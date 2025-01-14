from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('best_model.pkl', 'rb'))

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

    levels_dict = {
        'Low': 1,
        'Medium': 2,
        'High': 0
    }

    gender_dict = {
        'Male': 1,
        'Female': 0 
    }
    desc_dict = {
        'Yes': 1,
        'No': 0
    }

    # Get Values
    age = request.form['Age']
    gender = request.form['Gender']
    exercise = request.form['Exercise Habits']
    smoking = request.form['Smoking']
    fhd = request.form['Family Heart Disease']
    diabetes = request.form['Diabetes']
    bmi = request.form['BMI']
    hbp = request.form['High Blood Pressure']
    alcohol = request.form['Alcohol Consumption']
    stress = request.form['Stress Level']
    sleep = request.form['Sleep Hours']
    sugar = request.form['Sugar Consumption']

    gender = gender_dict[gender]

    smoking = desc_dict[smoking]
    fhd = desc_dict[fhd]
    diabetes = desc_dict[diabetes]
    hbp = desc_dict[hbp]


    exercise = levels_dict[exercise]
    alcohol = levels_dict[alcohol]
    stress = levels_dict[stress]
    sugar = levels_dict[sugar]
    
    data = pd.DataFrame({'Age': age, 
                         'Gender': gender, 
                         'Exercise Habits': exercise,
                         'Smoking': smoking, 
                         'Family Heart Disease': fhd,
                         'Diabetes': diabetes,
                         'BMI': bmi,
                         'High Blood Pressure': hbp,
                         'Alcohol Consumption': alcohol,
                         'Stress Level': stress,
                         'Sleep Hours': sleep,
                         'Sugar Consumption': sugar}, index=[0])

    prediction = f"Heart Disease Status: {model.predict(data)[0]}"

    if prediction == 1:
            prediction = "true"
    else:
        prediction = "false"

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