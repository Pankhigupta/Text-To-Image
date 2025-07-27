import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load model (only once)


@st.cache_resource
def load_pipeline():
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe


pipe = load_pipeline()

# UI
st.set_page_config(page_title="Free AI Image Generator", layout="centered")
st.title("🎨 AI Image Generator ")

prompt = st.text_area("Enter your prompt here", height=100)

if st.button("Generate Image"):
    if not prompt:
        st.warning("Please enter a prompt to generate an image.")
    else:
        with st.spinner("Generating image..."):
            image = pipe(prompt).images[0]
            st.image(image, caption="Generated Image",
                     use_container_width=True)
