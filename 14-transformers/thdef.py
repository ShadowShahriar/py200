from dotenv import load_dotenv
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
print("✅ Disabling TensorFlow logging")

load_dotenv()
print("✅ Loading environment variables")

print("✅ Attempting to login to Hugging Face...")

from huggingface_hub import login

login(token=os.getenv("HUGGING_FACE_ACCESS_TOKEN"))
print("✅ Successfully logged in")

print("✅ Initiating local model...")

from transformers import pipeline

# === https://huggingface.co/arpanghoshal/EmoRoBERTa ===
sentiment = pipeline("sentiment-analysis", model="arpanghoshal/EmoRoBERTa")

print("✅ Local model is ready")
