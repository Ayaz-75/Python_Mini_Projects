# =============================================
# 🖼️ Image Resizer Project - Full Script
# Features: Resize, Aspect Ratio, Batch, Format, Visualization
# =============================================

from PIL import Image
import os
import matplotlib.pyplot as plt

# -----------------------------
# Paths
# -----------------------------
input_folder = "images_input"
output_folder = "images_output"
batch_output_folder = os.path.join(output_folder, "outputs")

# Ensure output folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(batch_output_folder, exist_ok=True)

# -----------------------------
# 1 - Load and Test First Image
# -----------------------------
first_images = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
if first_images:
    first_image = first_images[0]
    img = Image.open(os.path.join(input_folder, first_image))
    print(f"Loaded image: {first_image}, size: {img.size}")
else:
    print("No images found in images_input folder!")

# -----------------------------
# 2 - Basic Resize (Fixed 256x256)
# -----------------------------
for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    
    if not os.path.isfile(img_path):
        continue

    img = Image.open(img_path)
    resized_img = img.resize((256, 256), Image.Resampling.LANCZOS)
    resized_img.save(os.path.join(output_folder, img_name))
    print(f"{img_name} resized to {resized_img.size}")

# -----------------------------
# 3 - Aspect Ratio Preservation
# -----------------------------
for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    
    if not os.path.isfile(img_path):
        continue

    img = Image.open(img_path)
    img.thumbnail((256, 256), Image.Resampling.LANCZOS)
    img.save(os.path.join(output_folder, img_name))
    print(f"{img_name} resized with aspect ratio: {img.size}")

# -----------------------------
# 4 - Batch Resize with Subfolders
# -----------------------------
for root, dirs, files in os.walk(input_folder):
    for file in files:
        img_path = os.path.join(root, file)
        if not os.path.isfile(img_path):
            continue

        img = Image.open(img_path)
        img.thumbnail((256, 256), Image.Resampling.LANCZOS)
        
        # Preserve folder structure
        relative_path = os.path.relpath(root, input_folder)
        save_folder = os.path.join(batch_output_folder, relative_path)
        os.makedirs(save_folder, exist_ok=True)
        img.save(os.path.join(save_folder, file))
        print(f"{file} saved to {save_folder}")

# -----------------------------
# 5 - Image Format Conversion (to JPG)
# -----------------------------
for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)
    if not os.path.isfile(img_path):
        continue

    img = Image.open(img_path)
    base_name = os.path.splitext(img_name)[0]
    img.convert('RGB').save(os.path.join(output_folder, f"{base_name}.jpg"))
    print(f"{img_name} converted to {base_name}.jpg")

# -----------------------------
# 6 - Visualization: Image Size Distribution
# -----------------------------
sizes = []
for img_name in os.listdir(output_folder):
    img_path = os.path.join(output_folder, img_name)
    if not os.path.isfile(img_path):
        continue

    img = Image.open(img_path)
    sizes.append(img.size[0] * img.size[1])

if sizes:
    plt.hist(sizes, bins=10, color='green', alpha=0.7)
    plt.title('Image Size Distribution')
    plt.xlabel('Pixel Count')
    plt.ylabel('Number of Images')
    plt.show()
else:
    print("No images to plot.")




# # 1- Setup + Test Image

# # Tasks:
# # Create folder Image_Resizer with subfolders images_input & images_output.
# # Download 5 sample images (can be PNG or JPG) and place in images_input.
# # Install Python + Pillow library (pip install pillow) for image operations.


# from PIL import Image
# import os
# import matplotlib.pyplot as plt


# input_folder = "images_input"
# output_folder = "images_output"



# # loading first image
# first_image = os.listdir(input_folder)[0]

# img = Image.open(os.path.join(input_folder, first_image))
# print(f"Loaded image: {first_image}, size: {img.size}")


# # 2 – Basic Resize
# # Tasks:
# # Resize an image to fixed dimensions, e.g., 256x256.


# for img_name in os.listdir(input_folder):
#     img_path = os.path.join(input_folder, img_name)

#     img = Image.open(img_path)
#     resized_img = img.resize((256, 256), Image.Resampling.LANCZOS)
#     resized_img.save(os.path.join(output_folder, img_name))
#     print(f"{img_name} resized to {resized_img.size}")


# # 3 – Aspect Ratio Preservation

# # Tasks:
# # Resize while preserving aspect ratio.

#     img.thumbnail((256, 256), Image.Resampling.LANCZOS)  # preserves aspect ratio
#     img.save(os.path.join(output_folder, img_name))
#     print(f"{img_name} resized with aspect ratio: {img.size}")


# # 4 – Batch Resize with Subfolders
# # Tasks:
# # Handle multiple input subfolders and resize all images.

# path_f = "images_output/outputs"
# for root, dirs, files in os.walk(input_folder):
#     for file in files:
#         img_path = os.path.join(root, file)
#         img = Image.open(img_path)
#         img.thumbnail((256, 256), Image.Resampling.LANCZOS)
#         # Preserve folder structure
#         relative_path = os.path.relpath(root, input_folder)
#         save_folder = os.path.join(path_f, relative_path)
#         os.makedirs(save_folder, exist_ok=True)
#         img.save(os.path.join(save_folder, file))
#         print(f"{file} saved to {save_folder}")


# # 5 – Image Format Conversion

# # Tasks:
# # Convert all images to a single format (e.g., JPG).

# for img_name in os.listdir(input_folder):
#     img = Image.open(os.path.join(input_folder, img_name))
#     base_name = os.path.splitext(img_name)[0]
#     img.convert('RGB').save(os.path.join(output_folder,  f"{base_name}.jpg"))
#     print(f"{img_name} converted to {base_name}.jpg")


# output_folder = 'images_output'
# sizes = []

# for img_name in os.listdir(output_folder):
#     img = Image.open(os.path.join(output_folder, img_name))
#     sizes.append(img.size[0] * img.size[1])

# plt.hist(sizes, bins=10, color='green', alpha=0.7)
# plt.title('Image Size Distribution')
# plt.xlabel('Pixel Count')
# plt.ylabel('Number of Images')
# plt.show()