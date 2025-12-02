from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

# Load your trained model
model = load_model('final_model.keras')

# Get input shape dynamically
MODEL_HEIGHT = model.input_shape[1]
MODEL_WIDTH = model.input_shape[2]

def getPrediction(img_path):
    # Load image and resize to model input
    img = image.load_img(img_path, target_size=(MODEL_HEIGHT, MODEL_WIDTH))
    img_array = image.img_to_array(img) / 255.0  # normalize
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

    # Get model predictions
    probabilities = model.predict(img_array)[0]
    
    organic_prob = probabilities[0]  # assuming class 0 is Organic
    # Apply threshold logic
    if organic_prob < 0.3:
        label = "Organic"
        confidence = round(organic_prob * 100, 2)
    else:
        label = "Recycle"
        confidence = round((1 - organic_prob) * 100, 2)

    return label, confidence
