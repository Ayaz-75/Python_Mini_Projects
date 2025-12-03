import numpy as np
import pandas as pd

data = pd.read_csv('./data/diabetes.csv')
glucose = np.array(data['Glucose'])

print("Max:", np.max(glucose))
print("Min:", np.min(glucose))
print("Mean:", np.mean(glucose))
