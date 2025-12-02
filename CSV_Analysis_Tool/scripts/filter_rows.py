import pandas as pd

data = pd.read_csv('./data/diabetes.csv')

high_glucose = data[data['Glucose'] > 120]
print(high_glucose.head())
print(data[data['Glucose'] > 150].head())
print(data[data['Glucose'] > 180].head())
print(data[data['BMI'] > 30].head())
print(data[data['Age'] >= 50].head())
print(data[data['Pregnancies'] >= 5].head())
print(data[data['Outcome'] == 1].head())
