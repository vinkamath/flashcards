import io

from include.basemodel import BaseModel

def gen_image(model : BaseModel, prompt):
	if model.name == "sdxl-1.0":
		# Define how many steps and what % of steps to be run on each experts (80/20) here
		n_steps = 25
		high_noise_frac = 0.8

		# run both experts
		image = model.base(
			prompt=prompt,
			num_inference_steps=n_steps,
			denoising_end=high_noise_frac,
			output_type="latent",
		).images
		pil_image = model.refiner(
			prompt=prompt,
			num_inference_steps=n_steps,
			denoising_start=high_noise_frac,
			image=image,
			output_type="pil"
		).images[0]
	elif model.name == "sdxl-turbo":
		pil_image = model.base(prompt=prompt, num_inference_steps=1, guidance_scale=0.0, output_type="pil").images[0]
	else:
		TypeError("Model {model.name} hasn't been implemented yet")

	# Create a BytesIO buffer and save the PIL image into this buffer
	buffer = io.BytesIO()
	pil_image.save(buffer, format='PNG')
	return buffer.getvalue()
