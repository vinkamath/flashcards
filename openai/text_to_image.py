import urllib.request
from openai import OpenAI
client = OpenAI()
object = input("Object to generate:")

response = client.images.generate(
  model="dall-e-3",
  prompt="Realistic looking " + object + " in the centre of the image on a solid white background and solid white margins",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
#urllib.request.urlretrieve(image_url, "generated_images/" + object + ".png")
