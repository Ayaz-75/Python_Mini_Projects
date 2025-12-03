title: "CSV Analysis Tool"
summary: |
A complete Python toolkit for loading, analyzing, visualizing, and generating
automated PDF reports from CSV datasets. Built for research workflows,
university applications, and hands-on data analysis practice.

project_structure: |
CSV_ANALYSIS_TOOL/
├── data/
│ └── diabetes.csv
│
├── scripts/
│ ├── column_stats.py
│ ├── filter_rows.py
│ ├── generate_report.py
│ ├── glucose_histogram.py
│ ├── load_csv.py
│ ├── multiple_plots.py
│ ├── numpy_basics.py
│ ├── pandas_numpy_stats.py
│ └── stats.py
│
├── README.md
└── report.pdf

features:

- name: "CSV Loader"
  description: "Loads CSV files reliably with error handling."
  file: "load_csv.py"

- name: "Column Statistics Generator"
  description: "Computes mean, median, max, and min for all numeric columns."
  file: "column_stats.py"

- name: "Advanced Row Filtering"
  description: "Extracts subsets of data based on clinical or statistical thresholds."
  file: "filter_rows.py"

- name: "NumPy Analytics"
  description: "Performs fast numerical computations using NumPy arrays."
  file: "numpy_basics.py"

- name: "Pandas + NumPy Integration"
  description: "Combines pandas DataFrames with NumPy arrays for efficient processing."
  file: "pandas_numpy_stats.py"

- name: "Data Visualization"
  description: "Generates histograms for glucose, BMI, age, and more."
  files:

  - "glucose_histogram.py"
  - "multiple_plots.py"

- name: "Automated PDF Report"
  description: "Creates polished PDF summaries with statistics and insights."
  file: "generate_report.py"

dataset:
name: "Pima Indians Diabetes Dataset"
details:
rows: 768
columns: 9
description: |
Contains medical diagnostic measurements (glucose, BMI, insulin,
pregnancies, outcome) used for diabetes prediction research.

installation:
requirements: - python >= 3.8 - pandas - numpy - matplotlib - reportlab
commands: - "pip install pandas numpy matplotlib reportlab"

usage:
run_examples: - "python scripts/load_csv.py" - "python scripts/column_stats.py" - "python scripts/filter_rows.py" - "python scripts/numpy_basics.py" - "python scripts/pandas_numpy_stats.py" - "python scripts/glucose_histogram.py" - "python scripts/multiple_plots.py"

report_generation:
command: "python scripts/generate_report.py"
output: "report.pdf"

outputs:

- "Automated PDF report"
- "Filtered CSV subsets"
- "Histogram visualizations"
- "Console-based descriptive statistics"

purpose: |
This repository is part of a structured, discipline-oriented learning program
aimed at developing strong fundamentals in data analysis, visualization,
statistics, and research communication.

author: "Ayaz Ali"
