from django.contrib import admin
from .models import PredictionResult

@admin.register(PredictionResult)
class PredictionResultAdmin(admin.ModelAdmin):
    list_display = ('predicted_label', 'confidence_percentage', 'created_at')
    list_filter = ('predicted_label', 'created_at')
    readonly_fields = ('created_at', 'image', 'predicted_label', 'confidence')
    ordering = ('-created_at',)