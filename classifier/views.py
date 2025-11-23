from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .services import DiseaseClassifier
from .utils import generate_confidence_chart
from .models import PredictionResult

def index(request):
    """
    Handles the file upload and displays the main page.
    """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # 1. Save the image to the database/filesystem first
            prediction_obj = form.save(commit=False)
            prediction_obj.predicted_label = "Pending..." # Placeholder
            prediction_obj.confidence = 0.0
            prediction_obj.save()

            # 2. Run the AI Analysis
            try:
                # Get file path from the saved object
                image_path = prediction_obj.image.path
                
                # Call Service Layer
                predictions = DiseaseClassifier.predict(image_path)
                
                # 3. Update the Database with results
                top_label = next(iter(predictions)) # Get the first key
                top_score = predictions[top_label]
                
                prediction_obj.predicted_label = top_label
                prediction_obj.confidence = top_score
                prediction_obj.save()

                # 4. Generate Chart
                chart_html = generate_confidence_chart(predictions)

                context = {
                    'prediction': prediction_obj,
                    'chart_html': chart_html,
                    'formatted_label': top_label.replace('Apple___', '').replace('_', ' '),
                    'confidence_percent': f"{prediction_obj.confidence * 100:.1f}" 
                }
                return render(request, 'classifier/result.html', context)

            except Exception as e:
                print(f"Error during prediction: {e}")
                # If error, delete the entry to prevent junk data
                prediction_obj.delete()
                form.add_error(None, "Error processing image. Please try again.")
    else:
        form = ImageUploadForm()

    return render(request, 'classifier/index.html', {'form': form})


def history(request):
    """
    Displays a list of past scans, excluding any that failed (stuck on 'Pending...').
    """
    # Get all records, newest first
    # Filter out any rows where the label is still "Pending..."
    scans = PredictionResult.objects.exclude(predicted_label='Pending...').order_by('-created_at')
    
    return render(request, 'classifier/history.html', {'scans': scans})