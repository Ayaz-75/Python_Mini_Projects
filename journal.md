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
