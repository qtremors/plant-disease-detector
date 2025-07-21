
import json
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing import image as tf_image
import plotly.graph_objs as go
import plotly.io as pio

from .forms import ImageUploadForm

# Load the trained model and class labels
MODEL_PATH = 'plant_disease_model.h5'
LABELS_PATH = 'class_labels.json'
model = tf.keras.models.load_model(MODEL_PATH)
with open(LABELS_PATH) as f:
    labels = json.load(f)

def predict_image(image_path):
    """Loads an image, preprocesses it, and returns the top 3 predictions."""
    img = tf_image.load_img(image_path, target_size=(224, 224))
    img_array = tf_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    predictions = model.predict(img_array)[0]

    # Get top 3 predictions
    top_indices = predictions.argsort()[-3:][::-1]
    top_predictions = {labels[str(i)]: float(predictions[i]) for i in top_indices}
    return top_predictions

def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            fs = FileSystemStorage()
            # Save the file and get its path
            filename = fs.save(uploaded_image.name, uploaded_image)
            image_url = fs.url(filename)
            image_path = fs.path(filename)

            # Get predictions
            predictions = predict_image(image_path)

            # Get the top prediction for display
            top_prediction_label = next(iter(predictions))
            top_prediction_confidence = predictions[top_prediction_label]

            # Create Plotly chart
            bar = go.Bar(
                x=list(predictions.values()),
                y=list(predictions.keys()),
                orientation='h'
            )
            fig = go.Figure(data=[bar])
            fig.update_layout(title_text='Prediction Confidence')
            chart_html = pio.to_html(fig, full_html=False)

            context = {
                'form': form,
                'image_url': image_url,
                'prediction_label': top_prediction_label.replace('_', ' '),
                'prediction_confidence': f"{top_prediction_confidence:.2%}",
                'chart_html': chart_html,
            }
            return render(request, 'classifier/result.html', context)
    else:
        form = ImageUploadForm()

    return render(request, 'classifier/index.html', {'form': form})