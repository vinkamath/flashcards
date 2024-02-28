import io
from pathlib import Path  
from PIL import Image
import img2pdf
   
def print_images(input_dir):
   out_filename = "output.pdf"

   png_files = []
   for path in Path(input_dir).glob('**/*.png'):
      png_files.append(path)

   combined_images = []
   for i in range(0, 8, 4):
         images = [Image.open(x) for x in png_files[i:i+4]]
         if images:
               # Assuming a letter size page printed at 300dpi
               page_width = int(8.5 * 250)
               page_height = 11 * 250
               img_width, img_height = images[0].size
               x_offset = (page_width - 2 *img_width)//4
               y_offset = (page_height - 2 *img_height)//4
               new_img = Image.new('RGB', (page_width, page_height), 'white')

               new_img.paste(images[0], (x_offset, y_offset))  
               new_img.paste(images[1], (page_width // 2 + x_offset, y_offset))
               new_img.paste(images[2], (x_offset, page_height// 2 + y_offset))
               new_img.paste(images[3], (page_width // 2 + x_offset, page_height // 2  + y_offset))


               byte_arr = io.BytesIO()
               new_img.save(byte_arr, format='PNG')
               byte_arr = byte_arr.getvalue()
               combined_images.append(byte_arr)

   with open(out_filename,"wb") as f:
         f.write(img2pdf.convert(combined_images))

   num_pages = len(combined_images)
   print(f"Wrote {num_pages} pages to: {out_filename}")

if __name__ == "__main__":
  print_images("generated_images/accepted/captioned")