README:
title: "# 🖼️ Image Resizer Project"
description: |
**Image Resizer** is a Python mini-project designed to help preprocess images for **Machine Learning**, **Deep Learning**, and **Computer Vision** tasks.  
 This tool allows you to: - Resize images to fixed dimensions - Preserve aspect ratios - Batch process folders of images - Convert image formats - Visualize image size distribution

folder_structure: |
**Folder Structure:**
`  Image_Resizer/
    ├── images_input/           # Original images (source)
    ├── images_output/          # Resized images (destination)
    ├── resize.py               # Main Python script
    ├── README.md               # This file
    └── report.pdf              # Summary of the project
 `

installation: | ## ⚙️ Installation 1. Install Python 3.8+  
 2. Install Pillow:
`bash
    pip install pillow
    ` 3. Optional: Install Matplotlib for visualizations:
`bash
    pip install matplotlib
    `

usage: | ## 🚀 Usage 1. Place your images in `images_input/` folder. 2. Run the script:
`python
    python resize.py
    ` 3. Check `images_output/` folder for resized images.

features: |

## ✨ Features

- **Resize to fixed dimensions:** e.g., 256x256 pixels
- **Preserve aspect ratio** with high-quality resampling
- **Batch processing** of folders and subfolders
- **Format conversion:** e.g., PNG → JPG
- **Multi-threaded processing** for faster resizing
- **Visualization:** Histogram of image sizes

example_code: | ## 💻 Example Code

````python
from PIL import Image
import os

    input_folder = 'images_input'
    output_folder = 'images_output'

    for img_name in os.listdir(input_folder):
        img_path = os.path.join(input_folder, img_name)
        img = Image.open(img_path)
        resized_img = img.resize((256, 256), Image.Resampling.LANCZOS)
        resized_img.save(os.path.join(output_folder, img_name))
        print(f"{img_name} resized to {resized_img.size}")
    ```

````
