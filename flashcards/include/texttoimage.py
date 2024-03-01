import os

from include.basemodel import BaseModel


def gen_image_from_prompt(model : BaseModel, prompt):
  if (model.family == "kandinsky"):
    from include.kandinsky import gen_image

  elif (model.family == "openai"):
    from include.dalle import gen_image
  
  elif (model.family == "sdxl"):
    from include.sdxl import gen_image 
  
  else:
      raise ValueError("Model {model} is not supported.")
 
  return gen_image(model, prompt)