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


heart_disease_data = pd.read_csv("HeartDiseasePredictor\heart.csv")

predict = "hd"

# Drop rows with missing values
heart_disease_data = heart_disease_data.dropna()

# PDA
# - age
# - sex
# - cp
# - trestbps
# - chol
# - fbs
# - restecg
# - thalach
# - exang
# - oldpeak
# - slope
# - ca
# - thal
# - hd


# Encode categorical variables
le = LabelEncoder() 
age = le.fit_transform(list(heart_disease_data['age']))
sex = le.fit_transform(list(heart_disease_data['sex']))
cp = le.fit_transform(list(heart_disease_data['cp']))
trestbps = le.fit_transform(list(heart_disease_data['trestbps']))
chol = le.fit_transform(list(heart_disease_data['chol']))
fbs = le.fit_transform(list(heart_disease_data['fbs']))
restecg = le.fit_transform(list(heart_disease_data['restecg']))
thalach = le.fit_transform(list(heart_disease_data['thalach'])) # heart defect thalacemia
exang = le.fit_transform(list(heart_disease_data['exang'])) # exercise induced angina
oldpeak = le.fit_transform(list(heart_disease_data['oldpeak']))
slope = le.fit_transform(list(heart_disease_data['slope']))
ca = le.fit_transform(list(heart_disease_data['ca']))
thal = le.fit_transform(list(heart_disease_data['thal']))
hd = le.fit_transform(list(heart_disease_data['hd']))
# two possibilities 1, 0 or yes and no



# Split data into features and target
x = list(zip(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)) # add vals
y = list(hd)

num_folds = 5
seed = 42

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

# RF is best model
predictive_models.append(("RF", RandomForestClassifier))
rf = RandomForestClassifier()
best_model = rf
best_model.fit(x_train, y_train)
y_pred = best_model.predict(x_test)
print(f"Best Model Accuracy Score on Test Set: {accuracy_score(y_test, y_pred)}")
print(f"Best Model Precision Score on Test Set: {precision_score(y_test, y_pred)}")
print(y_pred)


print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()