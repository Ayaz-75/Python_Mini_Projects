journal:
basics: - question: "What is a CSV?"
answer: >
A CSV (Comma Separated Values) file stores data separated by commas.
It is a lightweight alternative to Excel or spreadsheets.

    - question: "How does pandas read CSV?"
      code: |
        import pandas as pd
        df = pd.read_csv('filename.csv')

    - question: "What does .head() do?"
      answer: "Displays the first 5 rows of the dataset."

entries:

    - date: "2025-12-02"
      title: "Understanding Descriptive Statistics"
      details: >
        Learned statistical summaries using df.describe(): mean, median, std, quartiles.
        Median is more robust to outliers than mean.
      output: "Generated report.pdf using pandas + ReportLab."

    - date: "2025-12-02"
      title: "Filtering Medical Data"
      dataset: "Pima Indians Diabetes Dataset (768 rows)"
      filters_tested:
        - { condition: "Glucose > 120", result_rows: 349 }
        - { condition: "Glucose > 150", result_rows: 188 }
        - { condition: "BMI > 30", result_rows: 449 }
        - { condition: "Outcome = 1", result_rows: 268 }
      highlight: "Only 31 individuals meet all high-risk criteria."
      progress: "Implemented filter_rows.py"

    - date: "2025-12-03"
      title: "Day 4 – Functions + Modular Code"
      created:
        - "column_stats.py"
        - "stats.py"
      learned: >
        How functions improve modularity, reusability, and clarity.

    - date: "2025-12-04"
      title: "Day 5 – NumPy Basics"
      created:
        - "numpy_basics.py"
      learned: >
        Converted pandas columns to NumPy arrays. Calculated mean, min, max with NumPy.

    - date: "2025-12-05"
      title: "Day 6 – Pandas + NumPy Integration"
      created:
        - "pandas_numpy_stats.py"
      learned: >
        Looping through columns, converting each to a NumPy array, calculating statistics.

    - date: "2025-12-06"
      title: "Day 7 – Visualizations"
      created:
        - "glucose_histogram.py"
        - "multiple_plots.py"
      learned: >
        Built histograms for Glucose, BMI, and Age. Learned visualization basics.

    - date: "2025-12-06"
      title: "Report Generation"
      created:
        - "generate_report.py"
      learned: >
        Automated PDF generation for dataset statistics and summaries.
        Ready for professor email outreach.

project_status:
complete_scripts: - "load_csv.py" - "stats.py" - "column_stats.py" - "filter_rows.py" - "numpy_basics.py" - "pandas_numpy_stats.py" - "glucose_histogram.py" - "multiple_plots.py" - "generate_report.py"

    summary: >
      All analysis, stats, visualization, and reporting scripts completed.
      Project is fully functional and ready for GitHub + academic outreach.

git_commands:
push: |
git add .
git commit -m "Added full CSV Analysis Tool scripts, visualizations, updated journal and README"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CSV_ANALYSIS_TOOL.git
git push -u origin main

force_fix_remote: |
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CSV_ANALYSIS_TOOL.git
git push -u origin main

<!-- Q. What CSV is ?
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

| Condition              | Code Example                     | Result (rows) |
| ---------------------- | -------------------------------- | ------------- |
| Glucose > 120          | `data[data['Glucose'] > 120]`    | 349 patients  |
| Glucose > 150          | `data[data['Glucose'] > 150]`    | 188 patients  |
| Glucose > 180 (severe) | `data[data['Glucose'] > 180]`    | 66 patients   |
| BMI > 30 (obese)       | `data[data['BMI'] > 30]`         | 449 patients  |
| Age ≥ 50               | `data[data['Age'] >= 50]`        | 87 patients   |
| Pregnant ≥ 5 times     | `data[data['Pregnancies'] >= 5]` | 118 patients  |
| Diabetic patients only | `data[data['Outcome'] == 1]`     | 268 patients  |

# → Only 31 patients match all 3 risk factors!

#### Conclusion: Filtering lets us go from 768 rows → just the few patients who need urgent attention.

#### Today: Added real-world filter_rows.py with multiple thresholds + saved results -->
