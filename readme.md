# 🎨 AI Image Generator using Streamlit and Stable Diffusion

A simple, interactive Streamlit web app that generates images from textual prompts using the **Stable Diffusion v1.5** model from Hugging Face 🤗 `diffusers`.

---

## 🌐 Live Demo

https://text-to-imagez.streamlit.app

---

## 📸 Screenshots

>

| ![Screenshot 1](screenshots/Cats.png) | ![Screenshot 2](screenshots/IceCream.png) |

---

## 🚀 Features

- ✅ Generate images from natural language prompts
- ✅ GPU support using `torch.cuda`
- ✅ Fast image generation with optimized inference settings
- ✅ Clean, responsive Streamlit UI
- ✅ Efficient memory usage with `attention_slicing`

---

## 🧠 Tech Stack

| Tech                                                                           | Purpose                                  |
| ------------------------------------------------------------------------------ | ---------------------------------------- |
| [Streamlit](https://streamlit.io/)                                             | Frontend UI for user interaction         |
| [Hugging Face 🤗 diffusers](https://github.com/huggingface/diffusers)          | For loading and running Stable Diffusion |
| [PyTorch](https://pytorch.org/)                                                | Deep learning framework                  |
| [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | Text-to-image generation model           |
| [PIL](https://pillow.readthedocs.io/)                                          | Image handling and display               |

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/ai-image-generator.git
cd ai-image-generator
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
