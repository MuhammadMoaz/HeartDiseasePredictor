import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib as mp
from sklearn.preprocessing import LabelEncoder

heart_disease_data = pd.read_csv("heart_disease.csv")

predict = "Heart Disease Status"

for i in range (0, len(heart_disease_data)):
    heart_disease_data["ID"] = i
    i += 1



heart_disease_data.pop("Cholesterol Level")
heart_disease_data.pop("Blood Pressure")
heart_disease_data.pop("Low HDL Cholesterol")
heart_disease_data.pop("High LDL Cholesterol")
heart_disease_data.pop("Triglyceride Level")
heart_disease_data.pop("Fasting Blood Sugar")
heart_disease_data.pop("CRP Level")
heart_disease_data.pop("Homocysteine Level")

print(heart_disease_data)

# PDA
# - Age
# - Gender
# - Exercise Habits
# - Smoking
# - Family Heart Disease
# - Diabetes
# - BMI
# - High Blood Pressure [Optional]
# - Alcohol Consumption
# - Stress Level
# - Sleep Hours
# - Sugar Consumption

# Encode categorical variables
# label_encoder = LabelEncoder()
# heart_disease_data['Age'] = label_encoder.fit_transform(data['Age'])
# heart_disease_data['Gender'] = label_encoder.fit_transform(data['Gender'])
# heart_disease_data['Exercise Habits'] = label_encoder.fit_transform(data['Exercise Habits'])
# heart_disease_data['Smoking'] = label_encoder.fit_transform(data['Smoking'])
# heart_disease_data['Family Heart Disease'] = label_encoder.fit_transform(data['Gender'])
# heart_disease_data['Diabetes'] = label_encoder.fit_transform(data['Diabetes'])
# heart_disease_data['BMI'] = label_encoder.fit_transform(data['BMI'])
# heart_disease_data['High Blood Pressure'] = label_encoder.fit_transform(data['High Blood Pressure'])
# heart_disease_data['Alcohol Consumption'] = label_encoder.fit_transform(data['Alcohol Consumption'])
# heart_disease_data['Stress Level'] = label_encoder.fit_transform(data['Stress Level'])
# heart_disease_data['Sleep Hours'] = label_encoder.fit_transform(data['Sleep Hours'])
# heart_disease_data['Sugar Consumption'] = label_encoder.fit_transform(data['Sugar Consumption'])

# # Split data into features and target
# X = data.drop(['Rank', 'ID', 'GDP_diff', 'Country', 'Continent'], axis=1)
# y = data['Continent']

