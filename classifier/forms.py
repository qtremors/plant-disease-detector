from django import forms
from .models import PredictionResult

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = PredictionResult
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control form-control-lg', 
                'accept': 'image/*'
            })
        }