import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# -----------------------------
# Load Model
# -----------------------------

model = tf.keras.models.load_model(
    "rice_model.keras",
    compile=False
)


# Classes
classes = [
    "Arborio",
    "Basmati",
    "Ipsala",
    "Jasmine",
    "Karacadag"
]


# -----------------------------
# UI
# -----------------------------

st.title("🌾 Rice Image Classification")

st.write(
    "Upload a rice grain image"
)


uploaded_file = st.file_uploader(
    "Choose Image",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)


# -----------------------------
# Prediction
# -----------------------------

if uploaded_file is not None:

    try:

        image = Image.open(
            uploaded_file
        ).convert("RGB")


        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )


        image = image.resize(
            (224,224)
        )


        img_array = np.array(
            image
        )


        img_array = np.expand_dims(
            img_array,
            axis=0
        )


        prediction = model.predict(
            img_array
        )


        index = np.argmax(
            prediction
        )


        confidence = np.max(
            prediction
        )


        st.success(
            f"🌾 Rice Type: {classes[index]}"
        )


        st.write(
            f"Confidence: {confidence*100:.2f}%"
        )


    except Exception as e:

        st.error(
            "Prediction failed"
        )

        st.write(e)
