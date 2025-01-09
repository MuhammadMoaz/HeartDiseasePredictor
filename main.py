import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib as mp
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pickle


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
hbp = le.fit_transform(list(heart_disease_data['High Blood Pressure']))
alcohol = le.fit_transform(list(heart_disease_data['Alcohol Consumption']))
stress = le.fit_transform(list(heart_disease_data['Stress Level']))
sleep = le.fit_transform(list(heart_disease_data['Sleep Hours']))
sugar = le.fit_transform(list(heart_disease_data['Sugar Consumption']))
heart_disease = le.fit_transform(list(heart_disease_data['Heart Disease Status']))
# two possibilities yes and no

# high = 0, low = 1, med = 2
print(hbp[0])
print(hbp[1])
print(hbp[2])
print(hbp[3])


# Split data into features and target
x = list(zip(age, gender, exercise, smoking, family, diabetes, bmi, hbp, alcohol, stress, sleep, sugar))
y = list(heart_disease)

num_folds = 5
seed = 7

scoring = "accuracy"

# Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=seed)


predictive_models = []

# Initialize and add models to hashmap of all models
predictive_models.append(("NB", GaussianNB()))
predictive_models.append(("SVM", SVC()))
predictive_models.append(("GBM", GradientBoostingClassifier()))
predictive_models.append(("RF", RandomForestClassifier()))
predictive_models.append(("DTC", DecisionTreeClassifier()))


model_results = []
model_names = []

# determining best model
print("Performance on Training set")

# go through model list and use each one
for name, model in predictive_models:
    kfold = KFold(n_splits=num_folds,shuffle=True,random_state=seed)
    cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring="accuracy")
    # adding model name and accuracy to lists
    model_results.append(cv_results)
    model_names.append(name)
    # outputing results of model
    print(f"{name}: {cv_results.mean():,.6f} ({cv_results.std():,.6f})\n")

# bar graph comparison of models
fig = plt.figure()
fig.suptitle("Predictive Algorithm Comparison")
ax = fig.add_subplot(111)
plt.boxplot(model_results)
ax.set_xticklabels(model_names)
plt.show()

# SVM is best model
predictive_models.append(("SVM", SVC))
svm = SVC()
best_model = svm
best_model.fit(x_train, y_train)
y_pred = best_model.predict(x_test)
print(f"Best Model Accuracy Score on Test Set: {accuracy_score(y_test, y_pred)}")
print(y_pred)


print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

# Save the data to use in the software tool
with open('best_model.pkl', 'wb') as f:
    pickle.dump(svm, f)