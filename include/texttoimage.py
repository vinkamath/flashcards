import urllib.request
from openai import OpenAI
#from kandinsky3 import get_T2I_pipeline

import os

class textToImage():
  def __init__(self, output_dir="generated_images", model="dall-e-3", size_w="1024", size_h="1024", quality="standard", num_images=1):
     self.output_dir = output_dir
     self.model = model
     self.size = size_w + "x" + size_h
     self.quality = quality
     self.n = num_images
     self.client = OpenAI()

  def gen_image_from_prompt(self, category, object, prompt):
    #object = input("Object to generate:")
    #output_dir = "generated_images_dalle3"
    #category = "test"

    category = "general" if category == "" else category 
    category = category.lower().replace(" ", "_")
    image_dir = os.path.join(self.output_dir, category)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    filename = object.lower().replace(" ","_") + ".png"
    filepath = os.path.join(image_dir, filename)

    if (self.model in ["kandinsky3"]):
      t2i_pipe = get_T2I_pipeline('cuda', fp16=True)
      image = t2i_pipe(prompt)
      f = open(filepath, 'wb')
      f.write(image)

    elif (self.model in ["dall-e-2", "dall-e-3"]):
      response = self.client.images.generate(
        model=self.model,
        prompt=prompt,
        size=self.size,
        quality=self.quality,
        n=self.n,
      )
      image_url = response.data[0].url
      print(image_url)
      urllib.request.urlretrieve(image_url, filepath)
    
    else:
       raise ValueError("Model {self.model} is not supported.")
