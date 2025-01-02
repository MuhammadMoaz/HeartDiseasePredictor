import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib as mp
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report



heart_disease_data = pd.read_csv("heart_disease.csv")

predict = "Heart Disease Status"

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
le = LabelEncoder() 
ID = le.fit_transform(list(heart_disease_data['ID']))
age = le.fit_transform(list(heart_disease_data['Age']))
gender = le.fit_transform(list(heart_disease_data['Gender']))
exercise = le.fit_transform(list(heart_disease_data['Exercise Habits']))
smoking = le.fit_transform(list(heart_disease_data['Smoking']))
family = le.fit_transform(list(heart_disease_data['Family Heart Disease']))
diabetes = le.fit_transform(list(heart_disease_data['Diabetes']))
bmi = le.fit_transform(list(heart_disease_data['BMI']))
alcohol = le.fit_transform(list(heart_disease_data['Alcohol Consumption']))
stress = le.fit_transform(list(heart_disease_data['Stress Level']))
sleep = le.fit_transform(list(heart_disease_data['Sleep Hours']))
sugar = le.fit_transform(list(heart_disease_data['Sugar Consumption']))
heart_disease = le.fit_transform(list(heart_disease_data['Heart Disease Status']))



# Split data into features and target
X = list(zip(age, gender, exercise, smoking, family, diabetes, bmi, alcohol, stress, sleep, sugar))
y = list(heart_disease)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


predictive_models = []
# Initialize models
nb = GaussianNB()
svc = SVC()
gbc = GradientBoostingClassifier()
rfc = RandomForestClassifier()
dt = DecisionTreeClassifier()
xgb_model = xgb.XGBClassifier()

model_result = []
model_names = []

nb.fit(X_train, y_train)
nb_preds = nb.predict(X_test)
nb_acc = accuracy_score(y_test, nb_preds)

nb.fit(X_train, y_train)
nb_preds = nb.predict(X_test)
nb_acc = accuracy_score(y_test, nb_preds)

nb.fit(X_train, y_train)
nb_preds = nb.predict(X_test)
nb_acc = accuracy_score(y_test, nb_preds)

nb.fit(X_train, y_train)
nb_preds = nb.predict(X_test)
nb_acc = accuracy_score(y_test, nb_preds)