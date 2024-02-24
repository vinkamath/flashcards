import torch 

class BaseModel():
  def __init__(self, model_family = "openai", model_name="dall-e-3", size_w="1024", size_h="1024", quality="standard", num_images=1):
     self.size = size_w + "x" + size_h
     self.quality = quality
     self.n = num_images

     self.supported_models = {"openai": ["dall-e-2", "dall-e-3"],
                        "sdxl": ["sdxl-1.0", "sdxl-turbo"],
                        "kandinsky": ["kandinsky3"]
                        }
     if model_family in self.supported_models.keys():
        if model_name in self.supported_models[model_family]:
          self.family = model_family
          self.name = model_name
        else:
          print (f"Supported {model_family} models are {list(self.supported_models[model_family])}")
          raise TypeError(f"Unsupported model {model_name}")
     else:
        print(f"Supported model families: {list(self.supported_models.keys())}")
        raise TypeError(f"Unsupported family {model_family}.")

     # This is temporary hack. Move this to the respective classes
     if self.family == "sdxl":
      if self.name == "sdxl-turbo":
        from diffusers import AutoPipelineForText2Image
        self.base = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
        self.base.to("cuda")
      elif self.name == "sdxl-1.0":
        from diffusers import DiffusionPipeline
        # load both base & refiner
        self.base = DiffusionPipeline.from_pretrained(
          "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
        )
        self.base.to("cuda")
        self.refiner = DiffusionPipeline.from_pretrained(
          "stabilityai/stable-diffusion-xl-refiner-1.0",
          text_encoder_2=self.base.text_encoder_2,
          vae=self.base.vae,
          torch_dtype=torch.float16,
          use_safetensors=True,
          variant="fp16",
        )
        self.refiner.to("cuda")
