title: "CSV Analysis Tool"
description: >
A modular Python tool for loading, analyzing, visualizing, and generating reports
from CSV datasets. Uses Pandas, NumPy, Matplotlib, and ReportLab.

project_structure: |
CSV_ANALYSIS_TOOL/
│
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

- name: "Load CSV File"
  file: "load_csv.py"
  description: "Safely loads a CSV, handles missing files, returns a pandas DataFrame."

- name: "Column Statistics"
  file: "column_stats.py"
  description: "Computes mean, median, max, and min for every column."

- name: "Filtering Tool"
  file: "filter_rows.py"
  description: "Filters rows based on medical thresholds and saves filtered output."

- name: "NumPy Analytics"
  file: "numpy_basics.py"
  description: "Computes array-level stats using NumPy."

- name: "Pandas + NumPy Stats"
  file: "pandas_numpy_stats.py"
  description: "Loops through columns converting each to NumPy for statistics."

- name: "Visualizations"
  files:

  - "glucose_histogram.py"
  - "multiple_plots.py"
    description: "Histograms of Glucose, BMI, Age using Matplotlib."

- name: "PDF Report Generator"
  file: "generate_report.py"
  description: "Creates an automated PDF summary of the dataset."

dataset:
name: "Pima Indians Diabetes Dataset"
rows: 768
columns: 9
description: >
Contains diagnostic measurements such as glucose, BMI, insulin, pregnancies,
and diabetes outcome.

installation:
commands: - "pip install pandas numpy matplotlib reportlab"

usage:
scripts: - "python scripts/load_csv.py" - "python scripts/column_stats.py" - "python scripts/filter_rows.py" - "python scripts/numpy_basics.py" - "python scripts/pandas_numpy_stats.py" - "python scripts/glucose_histogram.py" - "python scripts/multiple_plots.py"

generate_report:
command: "python scripts/generate_report.py"

outputs:

- "report.pdf"
- "filtered CSV files"
- "PNG plots (if saved)"
- "Console statistics"

purpose: >
This tool is part of a structured learning roadmap through Python, data analysis,
visualization, and research-ready reporting for professor outreach.

author: "Ayaz Ali"
