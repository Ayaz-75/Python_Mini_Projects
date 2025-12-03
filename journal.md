journal:

fundamentals: - question: "What is a CSV?"
answer: |
A CSV (Comma Separated Values) file stores data in a comma-separated text format.
It is lightweight, human-readable, and an alternative to Excel spreadsheets.

    - question: "How does pandas read a CSV?"
      code: |
        import pandas as pd
        df = pd.read_csv('filename.csv')

    - question: "What does .head() do?"
      answer: "Displays the top 5 rows of a DataFrame."

entries:

    - date: "2025-12-02"
      title: "Descriptive Statistics Overview"
      concepts_learned:
        - mean
        - median
        - min / max
        - standard deviation
        - quartiles (25%, 50%, 75%)
      insights: |
        Median is more reliable when data contains outliers.
      progress: "Generated report.pdf using ReportLab."

    - date: "2025-12-02"
      title: "Filtering Real Medical Data"
      dataset: "Pima Indians Diabetes Dataset"
      filter_tests:
        glucose:
          ">120": 349
          ">150": 188
          ">180": 66
        BMI:
          ">30": 449
        Age:
          ">=50": 87
        Pregnancies:
          ">=5": 118
        Outcome:
          diabetic_only: 268
      insight: "Only 31 patients meet all severe-risk conditions."
      progress: "Created filter_rows.py and tested filters."

    - date: "2025-12-03"
      title: "Day 4 – Functional Programming"
      created_files:
        - "column_stats.py"
        - "stats.py"
      reflections: |
        Functions improve organization, reusability, clarity, and testing.

    - date: "2025-12-04"
      title: "Day 5 – NumPy Foundations"
      created_files:
        - "numpy_basics.py"
      reflections: |
        Learned NumPy array operations and statistical computations.

    - date: "2025-12-05"
      title: "Day 6 – Pandas + NumPy Integration"
      created_files:
        - "pandas_numpy_stats.py"
      reflections: |
        Looping through DataFrame columns and converting to NumPy arrays
        helps with performance and deeper numerical understanding.

    - date: "2025-12-06"
      title: "Day 7 – Data Visualization"
      created_files:
        - "glucose_histogram.py"
        - "multiple_plots.py"
      reflections: |
        Experimented with Matplotlib plotting for glucose, BMI, and age.
        Learned about bins, labels, titles, and showing plots.

    - date: "2025-12-06"
      title: "Automated Reporting System"
      created_files:
        - "generate_report.py"
      reflections: |
        Successfully generated a PDF with dataset statistics.
        This report can now be attached to professor outreach emails.

project_summary:
completed_scripts: - "load_csv.py" - "stats.py" - "column_stats.py" - "filter_rows.py" - "numpy_basics.py" - "pandas_numpy_stats.py" - "glucose_histogram.py" - "multiple_plots.py" - "generate_report.py"
status: |
The project is fully functional, modular, and research-ready.
All core tasks—loading, analysis, filtering, visualization, and report creation—are complete.

git:
push_commands: |
git add .
git commit -m "Completed CSV Analysis Tool: scripts, visualizations, journal, README"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CSV_ANALYSIS_TOOL.git
git push -u origin main

fix_remote: |
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/CSV_ANALYSIS_TOOL.git
git push -u origin main
