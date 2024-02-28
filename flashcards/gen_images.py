import os
from include.texttoimage import gen_image_from_prompt
from include.basemodel import BaseModel

def gen_images(output_dir):
    target_list_filename = 'flashcards.txt'
    MAX_IMAGES = 1
    model_family = "openai"
    model_name = "dall-e-3"

    image_cnt = 0
    current_dir = os.path.dirname(os.path.abspath(__file__))
    namelist_file = os.path.join(current_dir, target_list_filename)

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
            image_dir = os.path.join(output_dir, model_name, category)
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
                    image_model = BaseModel(model_family, model_name)
                print(category + ": " + object) 
                prompt = "side view photo of a single " + object + "on a light background, digital color camera" 
                image = gen_image_from_prompt(image_model, prompt)
                f = open(filepath, 'wb')
                f.write(image)

            image_cnt += 1
            if image_cnt >= MAX_IMAGES:
                break

if __name__ == "__main__":
  output_dir = "generated_images"
  gen_images(output_dir)                 
