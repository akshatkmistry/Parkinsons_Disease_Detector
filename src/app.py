import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the model
model = load_model('./models/parkinson_model_2.h5')

st.title("Parkinson's Disease Detection")
st.write("Upload a spiral drawing image to predict if it indicates Parkinson's disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and preprocess the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)  # Load as grayscale
    img = cv2.resize(img, (128, 128))
    img = img / 255.0  # Normalize as in training
    img = np.expand_dims(img, axis=-1)  # Add channel dimension: (256, 256, 1)
    img = np.expand_dims(img, axis=0)  # Add batch dimension: (1, 256, 256, 1)

    # Predict
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)  # Get class index (0 or 1)
    result = "Healthy" if predicted_class == 0 else "Parkinson's"
    confidence = prediction[0][predicted_class]  # Confidence for the predicted class

    st.image(uploaded_file, caption="Uploaded Spiral", use_column_width=True)
    st.write(f"Prediction: **{result}** (Confidence: {confidence:.2f})")

st.write("Note: This model is trained on spiral drawings and achieves 73.33% accuracy.")