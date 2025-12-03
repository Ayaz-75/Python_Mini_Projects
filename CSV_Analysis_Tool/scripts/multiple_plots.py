import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/diabetes.csv')
columns_to_plot = ['Glucose', 'BMI', 'Age']

for col in columns_to_plot:
    plt.hist(data[col], bins=20, alpha=0.7)
    plt.title(f'{col} Distribution')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()
