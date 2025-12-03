## journal:

intro:
basics: - question: "📌 What is a CSV?"
answer: >
A **CSV (Comma Separated Values)** file stores data separated by commas.
It's a lightweight alternative to Excel.

- question: "🐼 How does pandas read CSV?"
- code:

```Python
          import pandas as pd
          df = pd.read_csv('filename.csv')
```

      - question: "🔍 What does df.head() show?"
        answer: "The first 5 rows of the dataset — a quick preview."

#### entries:

- date: "📅 2025-12-02"
  title: "📊 Understanding Descriptive Statistics"
  details: > - Learned statistical concepts using **df.describe()** including mean, median,
  standard deviation, quartiles, and distribution insights.

  **Insight:**
  Median is much more reliable than mean when the data contains outliers.
  output: "Generated the first version of **report.pdf**."

- date: "📅 2025-12-02"
  title: "🩺 Filtering Diabetes Dataset"
  dataset: >
  Working with the **Pima Indians Diabetes Dataset (768 rows)**.
  filters_tested: - { condition: "Glucose > 120", result_rows: 349 } - { condition: "Glucose > 150", result_rows: 188 } - { condition: "BMI > 30", result_rows: 449 } - { condition: "Outcome = 1 (diabetic)", result_rows: 268 }
  highlight: "🔥 Only **31 patients** meet ALL high-risk medical criteria."
  progress: "Created filter_rows.py implementing multi-level medical filtering."

- date: "📅 2025-12-03"
  title: "🧩 Day 4 – Python Functions"
  created:

  - "column_stats.py"
  - "stats.py"
    learned: >
    - Functions helped turn scripts into reusable, clean modules.

- date: "📅 2025-12-04"
  title: "🧮 Day 5 – NumPy Basics"
  created:

  - "numpy_basics.py"
    learned: >
    - Converted pandas columns → NumPy arrays and computed array stats.

- date: "📅 2025-12-05"
  title: "🔗 Day 6 – Pandas + NumPy Integration"
  created:

  - "pandas_numpy_stats.py"
    learned: >
    - Looping over dataset columns and computing statistics efficiently.

- date: "📅 2025-12-06"
  title: "📉 Day 7 – Visualizations with Matplotlib"
  created:

  - "glucose_histogram.py"
  - "multiple_plots.py"
    learned: >
    - Built histograms for Glucose, BMI, and Age. Learned plotting aesthetics.

- date: "📅 2025-12-06"
  title: "📝 Report Automation"
  created:
  - "generate_report.py"
    learned: >
    - Generated a polished PDF research report using ReportLab

#### project_status:

**complete_scripts:**

- "load_csv.py"
- "stats.py"
- "column_stats.py"
- "filter_rows.py"
- "numpy_basics.py"
- "pandas_numpy_stats.py"
- "glucose_histogram.py"
- "multiple_plots.py"
- "generate_report.py"

#### summary: >

      The project is now fully functional: data loading, statistics, filtering,
      visualizations, and automated reporting — all done.

## 2025-12-03 – Image Resizer Project

### What is PIL (Pillow)?

- **PIL** = Python Imaging Library
- **Pillow** = modern, actively maintained fork of PIL
- The gold standard for opening, manipulating, and saving images in Python

### Why Pillow?

```python
from PIL import Image
img = Image.open("photo.jpg")  # Supports JPEG, PNG, WebP, BMP, TIFF, etc.
```

## 1 – Setup + Test Image"

tasks:

- Create `Image_Resizer` folder with subfolders `images_input` & `images_output`
- Download 5 sample images and place in `images_input`
- Install Python + Pillow library (`pip install pillow`)

##### notes:

      - Understand **PIL** library
      - Learn how to open an image and check its **size**
      - Difference between original and resized images

## 2 – Basic Resize

tasks:

- Resize an image to **256x256** - Save resized images to `images_output`

##### notes:

      - `resize()` method
      - Aspect ratio may be distorted if fixed size is used
      - Importance of consistent image size for ML

## 3 – Aspect Ratio Preservation

tasks:

- Use `thumbnail()` to resize while **preserving aspect ratio**

##### notes:

      - Difference between `resize()` and `thumbnail()`
      - Aspect ratio preservation helps avoid distorted images in ML

## 4 – Batch Resize with Subfolders

tasks:

- Resize all images in input folder, including subfolders
- Preserve folder structure in `images_output`

##### notes:

      - `os.walk()` for traversing folders
      - Benefits of batch preprocessing for large datasets

## 5 – Image Format Conversion

tasks:

- Convert all images to **JPG**
- Save converted images in output folder

##### notes:

      - Difference between PNG and JPG
      - Standardizing formats helps ML pipelines

## 6 – Multi-Threaded Resizing

tasks:

- Use `concurrent.futures.ThreadPoolExecutor` for faster batch processing

##### notes:

      - Benefits of parallel processing
      - Scales well for large datasets

## 7 – Visualization

tasks:

- Count images per folder
- Visualize image size distribution using Matplotlib

##### notes:

      - Learned skills:
        - PIL, batch processing, aspect ratio, multi-threading
        - Reflections on ML pipeline preparation

# summary:

## ✅ Week 1 Summary"

- Fully functional Image Resizer repo
- journal completed
