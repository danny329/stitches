from django import forms
from selection.models import Measurement
class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['profile_name', 'shirt_fit', 'neck', 'chest', 'waist', 'hips', 'shirt_length', 'shoulders', 'sleeve_length', 'cuff', 'arm_hole', 'biceps', 'height', 'weight']
