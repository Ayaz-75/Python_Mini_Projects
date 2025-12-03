import pandas as pd

def column_stats(file_path):
    data = pd.read_csv(file_path)
    stats_dict = {}
    for col in data.columns:
        stats_dict[col] = {
            'mean': data[col].mean(),
            'median': data[col].median(),
            'max': data[col].max(),
            'min': data[col].min()
        }
    return stats_dict

# Test
stats = column_stats('./data/diabetes.csv')
print(stats)
