import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HF_TOKEN")
client = InferenceClient(
    provider="fal-ai",
    api_key=os.environ["HF_TOKEN"],
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="stabilityai/stable-diffusion-3.5-large",
)
