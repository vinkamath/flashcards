import requests
from openai import OpenAI
from io import BytesIO

from include.basemodel import BaseModel

def gen_image(model : BaseModel, prompt):
	# Generate image URL
	client = OpenAI()
	response = client.images.generate(
		model = model.name,
		prompt = prompt,
		size = model.size,
		quality = model.quality,
		n = model.n,
		)
	image_url = response.data[0].url
	print(image_url)

	# Retrieve image from URL
	try:
		response = requests.get(image_url)
		response.raise_for_status()
	except requests.RequestException as err:
		print(f"Error downloading image: {err}")
		raise

	if response.status_code != 200:
		print(f"Error with request, status code: {response.status_code}")
	else:
		img_bytes = response.content
		img_stream = BytesIO(img_bytes)

	return img_stream.getvalue()