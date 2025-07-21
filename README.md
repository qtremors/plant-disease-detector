🌿 Plant Disease Detector
A web application built with Django and TensorFlow that uses a deep learning model to classify plant diseases from leaf images. Users can upload an image, and the application will predict the plant's health status, displaying the result with confidence scores.

(Replace the placeholder above with a screenshot of your application)

⚠️ Important: Current Model Limitations
This is a proof-of-concept implementation. The current model has been trained exclusively on apple leaf images.

Classes: The model can only identify the following four apple leaf conditions:

Apple Scab

Apple Black Rot

Apple Cedar Rust

Healthy Apple Leaf

Incorrect Predictions for Other Plants: If you upload an image of any other plant (e.g., a corn, potato, or tomato leaf), the model will still attempt to classify it as one of the four apple categories. It has no knowledge of other plant species.

To expand the model's capabilities, it must be retrained on a broader dataset including other plants (see "Future Improvements" section).

✨ Features
Image Upload: Simple web interface to upload a plant leaf image.

AI-Powered Prediction: Uses a fine-tuned MobileNetV2 model to classify the disease.

Confidence Scores: Displays a Plotly bar chart showing the model's confidence in the top 3 predictions.

Responsive UI: Clean interface built with Bootstrap that works on desktop and mobile.

🛠️ Technology Stack
Backend: Django

Machine Learning: TensorFlow, Keras

ML Model: MobileNetV2 (via Transfer Learning)

Data Visualization: Plotly

Frontend: HTML, Bootstrap 5

Core Libraries: Pillow, NumPy

🚀 Getting Started
Follow these instructions to set up and run the project locally.

1. Prerequisites
Python 3.8+

Git

2. Clone the Repository
git clone <your-repository-url>
cd plant-disease-detector

3. Set Up the Virtual Environment
Windows:

python -m venv venv
.\venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Prepare the Dataset for Training
Download: Download the "New Plant Diseases Dataset (Augmented)" from Kaggle.

Extract: Unzip the file into the project's root directory.

Filter for Apple Data: To replicate the current model, navigate into the dataset folders (.../train and .../valid) and delete all sub-folders except for the ones related to apples:

Apple___Apple_scab

Apple___Black_rot

Apple___Cedar_apple_rust

Apple___healthy

6. Train the Model
Run the training script. This will generate the plant_disease_model.h5 and class_labels.json files.

python train_model.py

7. Run the Django Application
python manage.py migrate
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/.

📈 Future Improvements
Expand the Dataset: Retrain the model on the full Plant Village dataset to include more plant species and diseases.

Add a Map Feature: Use JavaScript's Geolocation API and a library like Leaflet.js to allow users to (optionally) submit their location, plotting disease reports on a map.

Improve Model Accuracy: Experiment with more training epochs, different model architectures, or further fine-tuning of the base model layers.

Deployment: Deploy the application to a cloud platform like Heroku, AWS, or Google Cloud Platform for public access.# plant-disease-detector
A web application built with Django and TensorFlow that uses a deep learning model to classify plant diseases from leaf images. Users can upload an image, and the application will predict the plant's health status, displaying the result with confidence scores.
