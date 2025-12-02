# Classification-of-Waste-Material-using-Deep-Learning-CNN-
INTRODUCTION
This project implements a deep learning–based waste classification system capable of identifying whether a given waste image belongs to the Organic or Recyclable category. It uses a Convolutional Neural Network (CNN) trained on a structured dataset and deployed using a Flask-based web interface.
PROJECT OBJECTIVE
- Automate waste classification using CNN.
- Reduce manual labor and improve segregation accuracy.
- Provide a simple web interface for real-time predictions.
- Demonstrate practical application of deep learning in environmental sustainability.
SYSTEM OVERVIEW
The system allows users to upload an image of waste, after which the model preprocesses the image, performs classification using the trained CNN, and returns the result with a confidence score. The entire pipeline operates in real-time using Flask.
KEY FEATURES
- Binary waste classification (Organic / Recyclable).
- Flask-based web deployment.
- Automatic image preprocessing.
- High accuracy with deep learning.
- Lightweight and fast prediction.
FLOWCHART (LINK)
<img width="545" height="583" alt="image" src="https://github.com/user-attachments/assets/2ce3e76b-64cf-438b-b5dc-6a903015e413" />
 <img width="1024" height="1024" alt="Gemini_Generated_Image_gup590gup590gup5" src="https://github.com/user-attachments/assets/cc5898c3-a15f-4e02-8de6-a16803e1ad7a" />


PROJECT STRUCTURE
project/
├── index.py               # Flask backend
├── main.py                # Model prediction logic
├── train_model.py         # CNN training script
├── final_model.keras      # Trained model
├── templates/index.html   # Web UI
├── static/uploads/        # Uploaded images
└── Resources/Dataset/
    ├── Train/o , r
    └── Test/o , r

DATASET DETAILS
The dataset contains two categories of images:
- Organic: fruits, vegetables, food waste.
- Recyclable: plastic bottles, metal cans, glass items.
Images are arranged into Train and Test folders for CNN learning and evaluation. 
MODEL TRAINING DETAILS
- Image size: 64×64×3
- Optimizer: Adam
- Loss function: Binary Crossentropy
- Metrics: Accuracy
- Data Augmentation: rotation, flip, zoom, shift
The model is saved as final_model.keras.
 
 
PREDICTION PROCESS
1. User uploads an image.
2. Image is resized and normalized.
3. Model loads final_model.keras.
4. CNN predicts Organic or Recyclable.
5. Flask displays the result with confidence.
WEB APPLICATION WORKFLOW
User → Upload Image → Flask Backend → Preprocessing → CNN Model → Prediction → Display Output.
SAMPLE IMAGES (LINKS)
Organic Waste: Food_waste.jpg
 
Prediction: Organic
Confidence: ~85–95%
Recyclable Waste:
  
Prediction: Recyclable
Confidence: ~80–92%
Flask Interface Example: 
 


HOW TO RUN
1. Install dependencies:
   pip install tensorflow flask numpy pillow
2. Run Flask server:
   python index.py
3. Open browser:
   http://127.0.0.1:5000/
4. Upload a waste image to get prediction.
FUTURE ENHANCEMENTS
- Multi-class waste classification.
- Smart IoT integrated dustbins.
- Real-time video waste detection.
- Mobile application (TensorFlow Lite).
- Transfer learning models (ResNet, VGG16).
CONCLUSION
This project demonstrates the potential of deep learning in environmental applications. By automating waste classification, it reduces human effort, increases segregation accuracy, and promotes sustainable smart waste management practices
