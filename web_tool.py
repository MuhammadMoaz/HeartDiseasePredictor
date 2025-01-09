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
        0: 'No',
        1: 'Yes'
    }

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
    age = float(request.form['Age'])
    gender = gender_dict[request.form['Gender']]
    exercise_habits = levels_dict[request.form['Exercise Habits']]
    smoking = desc_dict[request.form['Smoking']]
    family_heart_disease = desc_dict[request.form['Family Heart Disease']]
    diabetes = desc_dict[request.form['Diabetes']]
    bmi = float(request.form['BMI'])
    high_blood_pressure = desc_dict[request.form['High Blood Pressure']]
    alcohol_consumption = levels_dict[request.form['Alcohol Consumption']]
    stress_level = levels_dict[request.form['Stress Level']]
    sleep_hours = float(request.form['Sleep Hours'])
    sugar_consumption = levels_dict[request.form['Sugar Consumption']]
    
    data = pd.DataFrame({'Age': [age], 
                         'Gender' : [gender], 
                         'Exercise Habits' : [exercise_habits],
                         'Smoking' : [smoking], 
                         'Family Heart Disease' : [family_heart_disease],
                         'Diabetes' : [diabetes],
                         'BMI' : [bmi],
                         'High Blood Pressure' : [high_blood_pressure],
                         'Alcohol Consumption' : [alcohol_consumption],
                         'Stress Level' : [stress_level],
                         'Sleep Hours' : [sleep_hours],
                         'Sugar Consumption': [sugar_consumption]})

    prediction = f"Heart Disease Status: {model.predict(data)}"

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