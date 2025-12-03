## journal:

intro:
basics: - question: "📌 What is a CSV?"
answer: >
A **CSV (Comma Separated Values)** file stores data separated by commas.
It's a lightweight alternative to Excel.

      - question: "🐼 How does pandas read CSV?"
        code: |
          import pandas as pd
          df = pd.read_csv('filename.csv')

      - question: "🔍 What does df.head() show?"
        answer: "The first 5 rows of the dataset — a quick preview."

#### entries:

    - date: "📅 2025-12-02"
      title: "📊 Understanding Descriptive Statistics"
      details: >
        Learned statistical concepts using **df.describe()** including mean, median,
        standard deviation, quartiles, and distribution insights.

        🧠 **Insight:**
        Median is much more reliable than mean when the data contains outliers.
      output: "Generated the first version of **report.pdf**."

    - date: "📅 2025-12-02"
      title: "🩺 Filtering Diabetes Dataset"
      dataset: >
        Working with the **Pima Indians Diabetes Dataset (768 rows)**.
      filters_tested:
        - { condition: "Glucose > 120", result_rows: 349 }
        - { condition: "Glucose > 150", result_rows: 188 }
        - { condition: "BMI > 30", result_rows: 449 }
        - { condition: "Outcome = 1 (diabetic)", result_rows: 268 }
      highlight: "🔥 Only **31 patients** meet ALL high-risk medical criteria."
      progress: "Created filter_rows.py implementing multi-level medical filtering."

    - date: "📅 2025-12-03"
      title: "🧩 Day 4 – Python Functions"
      created:
        - "column_stats.py"
        - "stats.py"
      learned: >
        Functions helped turn scripts into reusable, clean modules.

    - date: "📅 2025-12-04"
      title: "🧮 Day 5 – NumPy Basics"
      created:
        - "numpy_basics.py"
      learned: >
        Converted pandas columns → NumPy arrays and computed array stats.

    - date: "📅 2025-12-05"
      title: "🔗 Day 6 – Pandas + NumPy Integration"
      created:
        - "pandas_numpy_stats.py"
      learned: >
        Looping over dataset columns and computing statistics efficiently.

    - date: "📅 2025-12-06"
      title: "📉 Day 7 – Visualizations with Matplotlib"
      created:
        - "glucose_histogram.py"
        - "multiple_plots.py"
      learned: >
        Built histograms for Glucose, BMI, and Age. Learned plotting aesthetics.

    - date: "📅 2025-12-06"
      title: "📝 Report Automation"
      created:
        - "generate_report.py"
      learned: >
        Generated a polished PDF research report using ReportLab — ready for professor outreach.

#### project_status:

complete_scripts: - "load_csv.py" - "stats.py" - "column_stats.py" - "filter_rows.py" - "numpy_basics.py" - "pandas_numpy_stats.py" - "glucose_histogram.py" - "multiple_plots.py" - "generate_report.py"

#### summary: >

      The project is now fully functional: data loading, statistics, filtering,
      visualizations, and automated reporting — all done.

#### git_commands:

push: | # 🚀 Push to GitHub
git add .
git commit -m "Full CSV Analysis Tool: stats, visualizations, PDF report, journal + README"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CSV_ANALYSIS_TOOL.git
git push -u origin main

#### fix_remote: |

git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CSV_ANALYSIS_TOOL.git
git push -u origin main
