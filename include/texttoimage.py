import os

from include.basemodel import BaseModel


def gen_image_from_prompt(model : BaseModel, category, object, prompt):
  category = "general" if category == "" else category 
  category = category.lower().replace(" ", "_")
  image_dir = os.path.join(model.output_dir, category)
  if not os.path.exists(image_dir):
      os.makedirs(image_dir)
  filename = object.lower().replace(" ","_") + ".png"
  filepath = os.path.join(image_dir, filename)

  if (model.name in ["kandinsky3"]):
    from include.kandinsky import gen_image as gen_image
    image = gen_image(prompt)

  elif (model.name in ["dall-e-2", "dall-e-3"]):
    from include.dalle import gen_image as gen_image
    image = gen_image(model, prompt)
  
  else:
      raise ValueError("Model {model} is not supported.")

  f = open(filepath, 'wb')
  f.write(image)