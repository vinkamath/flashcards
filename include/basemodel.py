

class BaseModel():
  def __init__(self, output_dir="generated_images", model_name="dall-e-3", size_w="1024", size_h="1024", quality="standard", num_images=1):
     self.output_dir = output_dir
     self.name = model_name
     self.size = size_w + "x" + size_h
     self.quality = quality
     self.n = num_images