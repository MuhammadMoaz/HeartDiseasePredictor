import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset 
heart_data = pd.read_csv("heart_disease.csv")

# checking first and last 5 data rows and coloumns
print(heart_data.head())
print(heart_data.tail())

