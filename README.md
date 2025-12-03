# 📚 Python_Mini_Projects — CSV Analysis Tool & Image Resizer"

**This repository contains two Week-1 mini-projects** designed to build a foundation for **Machine Learning**, **Deep Learning**, and **Computer Vision**:
-     **CSV_Analysis_Tool** — a small pipeline to load, analyze and visualize CSV data (Pima Diabetes dataset).
      **Image_Resizer** — an image preprocessing tool to resize, preserve aspect ratio, batch process, convert formats, and visualize image distributions.
# Python Mini Projects  
A collection of clean, well-documented Python projects – perfect for learning & portfolio

**Repository Folder Structure**

```plaintext
Python_Mini_Projects/
├── CSV_Analysis_Tool/                  # Complete CSV + pandas project
│   ├── data/                           # sample CSVs (e.g., diabetes.csv)
│   ├── scripts/
│   │   ├── load_csv.py                 # Load and preview CSV
│   │   ├── stats.py                    # Column statistics
│   │   ├── filter_rows.py              # Row filtering examples
│   │   └── utils.py                    # Helper functions (optional)
│   ├── report.pdf                      # Short PDF summary of CSV analysis
│   └── README.md
│
├── Image_Resizer/                      # Batch image processor
│   ├── images_input/                   # Original images (source)
│   ├── images_output/                  # Resized images (destination)
│   ├── resize.py                       # Full pipeline (resize, thumbnail, batch, convert)
│   ├── README.md
│   └── report.pdf                      # Short PDF summary (screenshots + plots)
│
├── journal.md                          # Daily notes for Week 1 (CSV + Image Resizer)
└── LICENSE


```
## ⚙️ Installation (Environment & Libraries)
    1. Install **Python 3.8+** (recommended using Anaconda or system Python).
    2. Create and activate virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS / Linux
    venv\Scripts\activate      # Windows
    ```
    3. Install required packages:
    ```bash
    pip install pandas numpy matplotlib pillow
    ```
    4. (Optional) If you plan to generate PDFs programmatically:
    ```bash
    pip install reportlab
    ```
    5. Verify installations:
    ```bash
    python -c "import pandas, numpy, matplotlib, PIL; print('ok')"
    ```

## 🚀 How to use this repository — Quick Start
    1. Clone the repo and open it:
    ```bash
    git clone <your-repo-url>
    cd Python_Mini_Projects
    ```
    2. CSV Analysis:
       - Place `diabetes.csv` into `CSV_Analysis_Tool/data/`
       - Run the loader and stats scripts:
       ```bash
       python CSV_Analysis_Tool/scripts/load_csv.py
       python CSV_Analysis_Tool/scripts/stats.py
       python CSV_Analysis_Tool/scripts/filter_rows.py
       ```
       - Open `CSV_Analysis_Tool/report.pdf` for the summary and plots.
    3. Image Resizer:
       - Put raw images into `Image_Resizer/images_input/`
       - Run the full pipeline:
       ```bash
       python Image_Resizer/resize.py
       ```
       - Check `Image_Resizer/images_output/` and `Image_Resizer/images_output/outputs/` for processed images.
       - Open `Image_Resizer/report.pdf` for screenshots and histogram.

## 📊 CSV_Analysis_Tool — Details & Example Code
**Purpose:** Load a CSV, compute column-wise statistics, filter rows, and generate a short PDF report with plots and observations.

**Key scripts:**
    - `load_csv.py` — loads CSV and prints first rows.
    - `stats.py` — computes mean, median, max, min for each column.
    - `filter_rows.py` — example filters (e.g., `Glucose > 120`) and prints results.
    - `utils.py` — reusable functions (if present).

**Example — load_csv.py**
```python
        import pandas as pd

        ##  Load CSV
        ```data = pd.read_csv('../data/diabetes.csv')
        # Print first 10 rows
        print(data.head(10))
  ```

**Example — stats.py**
```python
    import pandas as pd
    data = pd.read_csv('../data/diabetes.csv')
    for col in data.columns:
        print(f"{col} - Mean: {data[col].mean()}, Median: {data[col].median()}, Max: {data[col].max()}, Min: {data[col].min()}")
    ```
```

## 🖼️ Image_Resizer — Details & Example Code
**Purpose:** Preprocess images (resize, maintain aspect ratio, batch process subfolders, convert formats, visualize). Fixed common issues: directory checks, permission errors, correct `resize()` usage, and safe file handling.

**Single-file pipeline:** `resize.py` — includes:
    - Loading / test image
    - Fixed-size resize (e.g., 256×256) using `Image.Resampling.LANCZOS`
    - Aspect ratio preservation with `.thumbnail()`
    - Batch processing with `os.walk()` and folder-structure preservation
    - Format conversion to `.jpg`
    - Visualization (histogram of pixel counts)

**Key example (snippet from `resize.py`):**
```python
    from PIL import Image
    import os
    import matplotlib.pyplot as plt

    input_folder = "images_input"
    output_folder = "images_output"
    os.makedirs(output_folder, exist_ok=True)

    for img_name in os.listdir(input_folder):
        img_path = os.path.join(input_folder, img_name)
        if not os.path.isfile(img_path):
            continue
        img = Image.open(img_path)
        resized_img = img.resize((256, 256), Image.Resampling.LANCZOS)
        resized_img.save(os.path.join(output_folder, img_name))
  ```


## ✨ Combined Features (Why this repo is useful)
**CSV Analysis Tool**
     - Quick CSV loading & preview
     - Column statistics (mean, median, min, max)
     - Row filtering demos
     - Plots ready for PDF reports
**Image Resizer**
     - Fixed-size and aspect-ratio resizing
     - Batch processing and folder structure preservation
     - Image format conversion (PNG → JPG)
     - Safe file checks to avoid PermissionErrors
     - Visualization of image size distribution for dataset insight

## 📌 Commit Rules & Journal
     - **Commit daily** (even partial work).
     - Update `README.md` and `journal.md` with progress each day.
     - `journal.md` summarizes Day 1–7 tasks, notes, and reflections for both projects.
     - `professors_spreadsheet.xlsx` stores the list of target professors + research links + emails.

## 🛠️ Troubleshooting — Common fixes
     - **PermissionError** when opening files:
     - Ensure you are opening a file, not a folder:
```python
      if not os.path.isfile(path):
          continue
      ```
      - **Pillow resize usage:**
      - Provide size as a tuple: `img.resize((256, 256), Image.Resampling.LANCZOS)`
      - **Aspect ratio preservation:**
      - Use `.thumbnail((w, h), Image.Resampling.LANCZOS)` instead of `resize()` if you want to keep aspect ratio.
      - **Large batches:**
      - Use `os.walk()` for subfolders and consider `concurrent.futures` for parallel processing.
```
## 💻 Example Commands (copy-paste)
      - Run CSV loader:
      ```bash
        python CSV_Analysis_Tool/scripts/load_csv.py
      ```
      - Run CSV stats:
      ```bash
      python CSV_Analysis_Tool/scripts/stats.py
      ```
      - Run image resizer:
      ```bash
      python Image_Resizer/resize.py
      ```
    

## **Happy coding!** ✨  
