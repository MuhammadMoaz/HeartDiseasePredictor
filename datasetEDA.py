import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset 
heart_data = pd.read_csv("heart_disease.csv")

# checking first and last 5 data rows and coloumns
print(heart_data.head())
print(heart_data.tail())
print(heart_data.shape)


print(heart_data.columns)
# unique values fsf
print(heart_data.nunique())
print(heart_data.info())

# age corrolation to heart disease
figure = plt.figure(figsize= (30, 30))
ax = figure.gca()

heart_data.hist(ax=ax, bins = 100, color = "purple")

plt.show()
# gender corrolation to heart disease

