Q. What CSV is ?
A. CSV is Comma Seperated Values file which stores the data in comma seperated form which is an alternative for spreadsheet or MS excel.

Q. How pandas reads CSV ?
A.

```Python
    import pandas as pd
    df = pd.read_csv('filename.csv')
```

Q. What .head() does ?
A. It shows the first few rows of the dataset.

# Journal – Python Mini Projects

## 2025-12-02 – Statistics Explained

When analyzing CSV files, `df.describe()` gives us these key values:

| Statistic  | Meaning                                                           |
| ---------- | ----------------------------------------------------------------- |
| **count**  | Number of non-missing values in the column                        |
| **mean**   | Average value (add all numbers → divide by count)                 |
| **median** | Middle value when sorted (50% percentile) – more robust than mean |
| **std**    | Standard deviation – how spread out the values are                |
| **min**    | Smallest value in the column                                      |
| **25%**    | First quartile – 25% of values are below this                     |
| **50%**    | Same as median                                                    |
| **75%**    | Third quartile – 75% of values are below this                     |
| **max**    | Largest value in the column                                       |

**Why median is often better than mean**:  
If salaries are [30k, 32k, 35k, 38k, 500k] → mean = ~127k (misleading!)  
→ median = 35k (realistic middle value)

Today: Generated automated `report.pdf` using pandas + ReportLab

## 2025-12-02 – Filtering Data with Real Diabetes Dataset

### Dataset

Using the famous **Pima Indians Diabetes Dataset** (`diabetes.csv`)  
→ 768 patients, 8 health measurements + Outcome (0 = no diabetes, 1 = diabetes)

### Key Filtering Examples Tested

| Condition              | Code Example                 | Result (rows) |
| ---------------------- | ---------------------------- | ------------- |
| Glucose > 120          | `df[df['Glucose'] > 120]`    | 349 patients  |
| Glucose > 150          | `df[df['Glucose'] > 150]`    | 188 patients  |
| Glucose > 180 (severe) | `df[df['Glucose'] > 180]`    | 66 patients   |
| BMI > 30 (obese)       | `df[df['BMI'] > 30]`         | 449 patients  |
| Age ≥ 50               | `df[df['Age'] >= 50]`        | 87 patients   |
| Pregnant ≥ 5 times     | `df[df['Pregnancies'] >= 5]` | 118 patients  |
| Diabetic patients only | `df[df['Outcome'] == 1]`     | 268 patients  |

# → Only 31 patients match all 3 risk factors!

#### Conclusion: Filtering lets us go from 768 rows → just the few patients who need urgent attention.

#### Today: Added real-world filter_rows.py with multiple thresholds + saved results
