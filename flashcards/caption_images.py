from glob import glob
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

input_dir = "generated_images/dalle-3"

# Get all PNGs from the input directory, recursirvely
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
image_dir = os.path.join(parent_dir, input_dir)
if not os.path.isdir(image_dir):
    raise FileNotFoundError(f"Directory not found: {image_dir}")
png_files = glob(image_dir + "/**/*.png", recursive=True)
jpg_files = glob(image_dir + "/**/*.jp*g", recursive=True)
all_image_files = png_files + jpg_files

# Caption images and write back with a different filename
for file in all_image_files:
    if "captioned" in file or "reject" in file:
            continue
    file_dir = os.path.dirname(file)
    filename_with_ext = os.path.basename(file)
    filename_wo_ext, ext = os.path.splitext(filename_with_ext)
    caption = filename_wo_ext.replace("_", " ").title()

    # Prepare draw/text settings
    image = Image.open(file)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Tahoma Bold.ttf", 60)
    _, _, text_width, text_height = draw.textbbox((0, 0), caption, font)

    # Calculate centered position
    x = (image.width - text_width) / 2
    y = 0.9 * image.height
    
    # Define the size of the area to sample around the pixel
    area_size = 100

    # Get the color of the pixels in the area around (x, y)
    area = image.crop((x - area_size//2, y - area_size//2, x + area_size//2, y + area_size//2))
    area_colors = np.array(area)
    # Calculate the average color of the area
    average_color = area_colors.mean(axis=(0, 1))
    # Choose a text color based on the brightness
    brightness = (average_color[0]*299 + average_color[1]*587 + average_color[2]*114) / 1000
    if brightness > 200:  # if the background is white or almost white
      text_color = (0, 0, 0)  # black
    elif brightness < 128:  # if the background is dark
      text_color = (255, 255, 255)  # white
    else:  # if the background is light
      text_color = (0, 0, 0)  # black
    print(f"Using {text_color} bcoz {brightness} for {caption}")
     
       
    # Draw text on image
    draw.text((x, y), caption, fill=text_color, font=font)

    # Save image
    out_dir = os.path.join(file_dir, "captioned")
    if not os.path.isdir(out_dir):
            os.mkdir(out_dir)
    out_file = os.path.join(file_dir, out_dir, filename_wo_ext + "_captioned" + ext)
    image.save(out_file)
