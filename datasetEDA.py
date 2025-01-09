import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset 
heart_data = pd.read_csv("heart_disease.csv")

# checking first and last 5 data rows and coloumns
print(heart_data.head())
print(heart_data.tail())
print(heart_data.shape)

# removing rows with empty cells
heart_data = heart_data.dropna()

print(heart_data.columns)
# unique values fsf
print(heart_data.nunique())
print(heart_data.info())


heart_data.plot(kind='box', subplots=True, layout=(3,5), figsize=(30, 10), color='blue')
plt.show()

# age corrolation to heart disease frequency
ages = heart_data["Age"]


# gender corrolation to heart disease


