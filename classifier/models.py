from django.db import models

class PredictionResult(models.Model):
    image = models.ImageField(upload_to='scans/%Y/%m/%d/')
    predicted_label = models.CharField(max_length=100)
    confidence = models.FloatField(help_text="Confidence score between 0 and 1")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def confidence_percentage(self):
        """Returns the confidence as an integer percentage (e.g., 98)."""
        return int(self.confidence * 100)

    def __str__(self):
        return f"{self.predicted_label} ({self.confidence:.1%})"