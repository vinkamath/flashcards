import os
import yaml

from include.texttoimage import gen_image_from_prompt
from include.basemodel import BaseModel

class GenerateImage():
    def __init__(self, config_dir='config', config_filename='generate.yaml') -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, config_dir, config_filename)
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        self.config_dirname = config_dir
        self.input_filename = config_data["general"]["input_filename"]
        self.max_images = config_data["general"]["max_images"]
        self.model_family = config_data["model"]["family"]
        self.model_name = config_data["model"]["name"]

    def generate(self, output_dir):
        image_cnt = 0
        current_dir = os.path.dirname(os.path.abspath(__file__))
        namelist_file = os.path.join(current_dir, self.config_dirname, self.input_filename)

        with open(namelist_file) as f:
            for line in f:
                line = line.strip()
                
                if not line:
                    continue            
                if line.startswith('#'):
                    category = line[1:].strip().lower().replace(" ", "_")
                    continue
                else:
                    object = line         

                # Create required directories 
                category = "general" if category == "" else category 
                category = category.lower().replace(" ", "_")
                image_dir = os.path.join(output_dir, self.model_name, category)
                if not os.path.exists(image_dir):
                    os.makedirs(image_dir)
                reject_dir = os.path.join(image_dir, "reject")
                if not os.path.exists(reject_dir):
                    os.makedirs(reject_dir)

                # Generate image only if it doesn't already exist
                filename = object.lower().replace(" ","_") + ".png"
                filepath = os.path.join(image_dir, filename)
                if not os.path.exists(filepath):
                    if 'image_model' not in locals():
                        image_model = BaseModel(self.model_family, self.model_name)
                    print(category + ": " + object) 
                    if "animal" in category:
                        prompt = "Full body shot side view of a single " + object + " in the style of a digital color photo"
                    elif "natural" in category:
                        prompt =  object + "in natural colors in the style of a digital color photo"
                    else:
                        prompt = "single " + object + " in the style of a professional product color photo"
                    image = gen_image_from_prompt(image_model, prompt)
                    f = open(filepath, 'wb')
                    f.write(image)

                image_cnt += 1
                if image_cnt >= self.max_images:
                    break

if __name__ == "__main__":
  output_dir = "generated_images"
  image = GenerateImage()
  image.generate(output_dir)                 
