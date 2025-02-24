import streamlit as st
import os
import base64
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Set environment variables
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# PredictionPipeline class
class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load the pre-trained model
        model_path = "artifacts/training/model.h5"  # Adjust path as needed for deployment
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        model = load_model(model_path)

        # Preprocess the input image
        imagename = self.filename
        if not os.path.exists(imagename):
            raise FileNotFoundError(f"Image file not found at {imagename}")
        
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0  # Normalize to [0, 1]
        test_image = np.expand_dims(test_image, axis=0)

        # Make prediction
        raw_prediction = model.predict(test_image)
        result = np.argmax(raw_prediction, axis=1)

        # Map prediction to class labels
        if result[0] == 1:
            prediction = "Normal"
        else:
            prediction = "Adenocarcinoma Cancer"

        # Return a dictionary with all relevant info
        return {
            "image": prediction,
            "raw_prediction": raw_prediction.tolist(),  # Convert numpy array to list for JSON compatibility
            "argmax_result": result.tolist(),           # Convert numpy array to list
        }

# Function to decode base64 image and save to file
def decodeImage(image_string, filename):
    """Decode a base64 string and save it as an image file."""
    with open(filename, "wb") as f:
        f.write(base64.b64decode(image_string))

# Streamlit UI
def main():
    st.title("Image Classification App")

    # Training section (optional, adjust based on your setup)
    if st.button("Train Model"):
        with st.spinner("Training in progress..."):
            os.system("python main.py")  # Ensure main.py exists if you keep this
        st.success("Training done successfully!")

    # Image upload and prediction section
    st.subheader("Upload an Image for Prediction")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Convert image to base64
        image_data = uploaded_file.read()
        b64_string = base64.b64encode(image_data).decode('utf-8')

        # Predict button
        if st.button("Predict"):
            with st.spinner("Predicting..."):
                # Decode and save the image
                filename = "inputImage.jpg"
                decodeImage(b64_string, filename)

                # Run prediction
                predictor = PredictionPipeline(filename)
                result = predictor.predict()

            # Display prediction results in the UI
            st.subheader("Prediction Results")
            st.write(f"**Final Prediction:** {result['image']}")
            st.write(f"**Raw Prediction (Probabilities):** {result['raw_prediction']}")
            st.write(f"**Argmax Result (Class Index):** {result['argmax_result']}")

if __name__ == "__main__":
    main()