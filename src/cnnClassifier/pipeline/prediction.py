import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Define the PredictionPipeline class
class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load the pre-trained model
        model_path = "model/model.h5"
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        model = load_model(model_path)
        print("Model loaded successfully.")

        # Preprocess the input image
        imagename = self.filename
        if not os.path.exists(imagename):
            raise FileNotFoundError(f"Image file not found at {imagename}")
        
        # Load and resize image to 224x224 (assuming this is the model's input size)
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)  # Convert to array
        print("Image shape after loading:", test_image.shape)  # Should be (224, 224, 3)

        # Normalize pixel values to [0, 1] (assuming this matches training preprocessing)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)  # Add batch dimension
        print("Image shape after preprocessing:", test_image.shape)  # Should be (1, 224, 224, 3)

        # Make prediction
        raw_prediction = model.predict(test_image)
        print("Raw prediction (probabilities):", raw_prediction)  # Raw output from the model
        result = np.argmax(raw_prediction, axis=1)
        print("Argmax result (class index):", result)  # Predicted class index

        # Map prediction to class labels
        if result[0] == 1:
            prediction = "Normal"
        else:
            prediction = "Adenocarcinoma Cancer"
        
        print(f"Final prediction: {prediction}")
        return [{"image": prediction}]

# Example usage
if __name__ == "__main__":
    # Replace 'path_to_your_image.jpg' with the actual path to your test CT scan image
    test_image_path = "path_to_your_image.jpg"
    
    # Instantiate the pipeline and predict
    try:
        pipeline = PredictionPipeline(test_image_path)
        result = pipeline.predict()
        print("Prediction result:", result)
    except Exception as e:
        print(f"An error occurred: {e}")