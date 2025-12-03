import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./data/diabetes.csv")

plt.hist(data["Glucose"], bins=20, color="blue", alpha=0.7)
plt.title("Glucose Distribution")
plt.xlabel("Glucose")
plt.ylabel("Count")

plt.show()
