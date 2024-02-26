import os
from pathlib import Path  
from PIL import Image  
import img2pdf
   
input_dir = 'generated_images/accepted/captioned'
out_filename = "output.pdf"

# Get all png files in the input directory
png_files = []
for path in Path(input_dir).glob('**/*.png'):
    png_files.append(path)

# Save pages as PDF 
with open(out_filename,"wb") as f:
    f.write(img2pdf.convert(png_files))
num_pages = len(png_files)
print(f"Wrote {num_pages} pages to: {out_filename}")