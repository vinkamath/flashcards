import urllib.request
from include import OpenAI
import os

class textToImage():
  def __init__(self, output_dir="generated_images", model="dall-e-3", size_w="1024", size_h="1024", quality="standard", num_images=1):
     self.output_dir = output_dir
     self.model = model
     self.size = size_w + "x" + size_h
     self.quality = quality
     self.n = num_images

     self.client = OpenAI()

  def gen_image_from_prompt(self, category, prompt):
    #object = input("Object to generate:")
    #output_dir = "generated_images_dalle3"
    #category = "test"
    print("Output dir: " + self.output_dir) 
    response = self.client.images.generate(
      model=self.model,
      prompt=prompt,
      size=self.size,
      quality=self.quality,
      n=self.n,
    )
    
    category = "general" if category == "" else category 
    category = category.lower().replace(" ", "_")

    image_url = response.data[0].url
    print(image_url)
    image_dir = os.path.join(self.output_dir, category)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    filename = object.lower().replace(" ","_") + ".png"
    filepath = os.path.join(image_dir, filename)
    urllib.request.urlretrieve(image_url, filepath)
