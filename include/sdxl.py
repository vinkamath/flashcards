from diffusers import DiffusionPipeline, AutoPipelineForText2Image
import torch

from include.basemodel import BaseModel

def gen_image(model : BaseModel, prompt):
	if model.name == "sdxl-1.0":
		# load both base & refiner
		base = DiffusionPipeline.from_pretrained(
			"stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
		)
		base.to("cuda")
		refiner = DiffusionPipeline.from_pretrained(
			"stabilityai/stable-diffusion-xl-refiner-1.0",
			text_encoder_2=base.text_encoder_2,
			vae=base.vae,
			torch_dtype=torch.float16,
			use_safetensors=True,
			variant="fp16",
		)
		refiner.to("cuda")

		# Define how many steps and what % of steps to be run on each experts (80/20) here
		n_steps = 25
		high_noise_frac = 0.8

		# run both experts
		image = base(
			prompt=prompt,
			num_inference_steps=n_steps,
			denoising_end=high_noise_frac,
			output_type="latent",
		).images
		image = refiner(
			prompt=prompt,
			num_inference_steps=n_steps,
			denoising_start=high_noise_frac,
			image=image,
		).images[0]
		return image
	elif model.name == "sdxl-turbo":
		pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
		pipe.to("cuda")
		return pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
	else:
		TypeError("Model {model.name} hasn't been implemented yet")