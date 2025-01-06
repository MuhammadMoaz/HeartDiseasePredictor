from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('best_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    heart_disease_dict = {
        0: 'no',
        1: 'yes'
    }

    #Get Values
    age = request.form['Age']
    gender = request.form['Gender']
    exercise_habits = request.form['Exercise Habits']
    smoking = request.form['Smoking']
    family_heart_disease = request.form['Family Heart Disease']
    diabetes = request.form['Diabetes']
    bmi = request.form['BMI']
    high_blood_pressure = request.form['High Blood Pressure']
    alcohol_consumption = request.form['Alcohol Consumption']
    stress_level = request.form['Stress Level']
    sleep_hours = request.form['Sleep Hours']
    sugar_consumption = request.form['Sugar Consumption']
    
    data = pd.DataFrame({'Age': age, 
                         'Gender' : gender, 
                         'Exercise Habits' : exercise_habits,
                         'Smoking' : smoking, 
                         'Family Heart Disease' : family_heart_disease,
                         'Diabetes' : diabetes,
                         'BMI' : bmi,
                         'High Blood Pressure' : high_blood_pressure,
                         'Alcohol Consumption' : alcohol_consumption,
                         'Stress Level' : stress_level,
                         'Sleep Hours' : sleep_hours,
                         'Sugar Consumption': sugar_consumption}, index=[0])

    prediction = f"Heart Disease Status: {heart_disease_dict[model.predict(data)][0]}"

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