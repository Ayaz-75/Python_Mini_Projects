import pandas as pd
import numpy as np

data = pd.read_csv('./data/diabetes.csv')

# Compute stats with NumPy
for col in data.columns:
    col_array = np.array(data[col])
    print(f"{col} - Mean: {np.mean(col_array)}, Max: {np.max(col_array)}, Min: {np.min(col_array)}")
