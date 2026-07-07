import streamlit as st
import keras
import numpy as np
from PIL import Image

model = keras.models.load_model("rice_model.keras")

classes = [
    "Arborio",
    "Basmati",
    "Ipsala",
    "Jasmine",
    "Karacadag"
]

st.title("🌾 Rice Classification")

file = st.file_uploader(
    "Upload rice image",
    type=["jpg","png","jpeg"]
)

if file:

    img = Image.open(file).convert("RGB")

    st.image(img)

    img = img.resize((224,224))

    img = np.array(img)

    img = np.expand_dims(img,0)

    pred = model.predict(img)[0]

    result = classes[np.argmax(pred)]

    confidence = np.max(pred)

    st.success(f"Rice Type: {result}")

    st.write(f"Confidence: {confidence*100:.2f}%")