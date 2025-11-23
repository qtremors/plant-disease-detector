import json
import numpy as np
import tensorflow as tf
from django.conf import settings
from tensorflow.keras.preprocessing import image as tf_image

class DiseaseClassifier:
    _model = None
    _labels = None

    @classmethod
    def _load_resources(cls):
        """
        Loads the model and labels only if they aren't loaded yet.
        This saves memory and makes the server start faster.
        """
        if cls._model is None:
            print("🧠 Loading ML Model into memory...") 
            cls._model = tf.keras.models.load_model(settings.ML_MODEL_PATH)
            
            with open(settings.ML_LABELS_PATH, 'r') as f:
                cls._labels = json.load(f)

    @classmethod
    def predict(cls, image_path):
        """
        Accepts an image path, returns a dictionary of the top 3 predictions.
        """
        # Ensure model is loaded
        cls._load_resources()

        # 1. Preprocess the image (resize and normalize)
        img = tf_image.load_img(image_path, target_size=(224, 224))
        img_array = tf_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize pixel values to [0, 1]

        # 2. Make Prediction
        predictions = cls._model.predict(img_array)[0]

        # 3. Get Top 3 Results
        # argsort returns indices of sorted values, we take last 3 and reverse them
        top_3_indices = predictions.argsort()[-3:][::-1]
        
        results = {}
        for i in top_3_indices:
            label_index = str(i)
            label_name = cls._labels.get(label_index, "Unknown")
            confidence = float(predictions[i])
            results[label_name] = confidence
            
        return results