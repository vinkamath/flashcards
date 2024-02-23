
class BaseModel():
  def __init__(self, output_dir="generated_images", category = "openai", model_name="dall-e-3", size_w="1024", size_h="1024", quality="standard", num_images=1):
     self.output_dir = output_dir
     self.size = size_w + "x" + size_h
     self.quality = quality
     self.n = num_images

     self.categories = {"openai": ["dall-e-2", "dall-e-3"],
                        "sdxl": ["sdxl-1.0", "sdxl-turbo"],
                        "kandinsky": ["kandinsky3"]
                        }
     if category in self.categories.keys():
        if model_name in self.categories[category]:
          self.category = category
          self.name = model_name
        else:
          print (f"Supported {category} models are {list(self.categories[category])}")
          raise TypeError(f"Unsupported model {model_name}")
     else:
        print(f"Supported categories: {list(self.categories.keys())}")
        raise TypeError(f"Unsupported category {category}.")