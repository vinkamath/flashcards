import os

from include.basemodel import BaseModel


def gen_image_from_prompt(model : BaseModel, category, object, prompt):
  if (model.category == "kandinsky"):
    from include.kandinsky import gen_image as gen_image

  elif (model.category == "openai"):
    from include.dalle import gen_image as gen_image
  
  else:
      raise ValueError("Model {model} is not supported.")
 
  return gen_image(model, prompt)