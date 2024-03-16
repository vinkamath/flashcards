import os
import yaml
from glob import glob
import numpy as np
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont

class CaptionImage():
  def __init__(self, config_dir='config', config_filename='caption.yaml') -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, config_dir, config_filename)
    with open(config_file, 'r') as file:
        config_data = yaml.safe_load(file)
    self.threshold_sample_area = config_data["thresholds"]["sample_area"]
    self.threshold_white = config_data["thresholds"]["white"]
    self.threshold_black = config_data["thresholds"]["black"]
    self.caption_fontname = config_data["caption"]["truetype_font_name"]
    self.caption_fontsize = config_data["caption"]["truetype_font_size"]
    self.caption_bottom_offset = config_data["caption"]["bottom_offset_percentage"]

  def gather_image_paths(self, image_dir: str) -> List[str]:
    # Get all PNGs from the input directory, recursirvely
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    image_dir = os.path.join(parent_dir, input_dir)
    if not os.path.isdir(image_dir):
        raise FileNotFoundError(f"Directory not found: {image_dir}")
    png_files = glob(image_dir + "/**/*.png", recursive=True)
    jpg_files = glob(image_dir + "/**/*.jp*g", recursive=True)
    return png_files + jpg_files

  def get_text_color(self, brightness: int) -> Tuple[int,int,int]:
        if brightness > self.threshold_white:  # if the background is white or almost white
          text_color = (0, 0, 0)  # black
        elif brightness < self.threshold_black:  # if the background is dark
          text_color = (255, 255, 255)  # white
        else:  # if the background is light
          text_color = (0, 0, 0)  # black
        return text_color

  def get_avg_brightness(self, image: Image.Image, x: int, y: int) -> int:
        # Get the color of the pixels in the area around (x, y)
        area_size = self.threshold_sample_area 
        area = image.crop((x, y, x + area_size//5, y + area_size//20)) # TBD: The aspect ratio is hardcoded here
        area_colors = np.array(area)
        average_color = area_colors.mean(axis=(0, 1))
        return (average_color[0]*299 + average_color[1]*587 + average_color[2]*114) / 1000 # TBD: More hardcoded values
        #draw.rectangle((x, y, x + area_size//5, y + area_size//20))

  def caption(self, input_dir: str) -> None:
    all_image_files = self.gather_image_paths(input_dir)
    if len(all_image_files) < 1:
        print(f"No files found for captioning in directory: {input_dir}")
        exit()

    # Caption images and write back with a different filename
    for file in all_image_files:
        if "captioned" in file or "reject" in file:
                continue
        #file_dir = os.path.dirname(file)
        filename_with_ext = os.path.basename(file)
        filename_wo_ext, ext = os.path.splitext(filename_with_ext)
        caption = filename_wo_ext.replace("_", " ").title()
        print(filename_wo_ext)

        image = Image.open(file)
        draw = ImageDraw.Draw(image)
        try:
          font = ImageFont.truetype(self.caption_fontname + ".ttf", self.caption_fontsize)
        except OSError as e:
          print(f"Unable to read font {self.caption_fontname}")
          raise
        except ValueError as e:
          print(f"Font {self.caption_fontname} size is 0")
          raise
        
        _, _, text_width, text_height = draw.textbbox((0, 0), caption, font)

        # Calculate centered position
        x = (image.width - text_width) / 2
        y = self.caption_bottom_offset * image.height
        brightness = self.get_avg_brightness(image, x, y) 
        
        # Save image
        draw.text((x, y), caption, fill=self.get_text_color(brightness), font=font)
        out_dir = os.path.join(input_dir, "captioned")
        if not os.path.isdir(out_dir):
                os.mkdir(out_dir)
        out_file = os.path.join(out_dir, filename_wo_ext + "_captioned" + ext)
        image.save(out_file)

if __name__ == "__main__":
  input_dir = "generated_images"
  image = CaptionImage()
  image.caption(input_dir)