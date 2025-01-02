import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib as mp

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
