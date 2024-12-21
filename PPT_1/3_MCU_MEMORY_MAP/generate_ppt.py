from PIL import Image
import os

# Step 1: Collect all image files in the current directory
image_files = [file for file in os.listdir() if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

# Step 2: Sort the images alphabetically (optional, for order)
image_files.sort()

# Step 3: Open images and prepare for PDF
if not image_files:
    print("No image files found in the current directory.")
else:
    # Open the first image to start the PDF
    image_list = []
    first_image = Image.open(image_files[0]).convert("RGB")  # Convert to RGB for PDF compatibility
    
    # Open remaining images and append to the list
    for img in image_files[1:]:
        img_obj = Image.open(img).convert("RGB")
        image_list.append(img_obj)
    
    # Step 4: Save images as a single PDF
    output_pdf = "PPT.pdf"
    first_image.save(output_pdf, save_all=True, append_images=image_list)
    
    print(f"PPT created successfully: {output_pdf}")

