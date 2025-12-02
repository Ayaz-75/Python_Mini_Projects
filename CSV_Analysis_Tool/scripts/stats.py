import pandas as pd

data = pd.read_csv("./data/diabetes.csv")

for col in data.columns:
    print(f"{col} - Mean: {data[col].mean()}, Median: {data[col].median()}, Max: {data[col].max()}, Min: {data[col].min()}")

