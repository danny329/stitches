from django import forms
from selection.models import Measurement
from django.contrib.auth.models import User
from .models import UserDetails
class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['profile_name', 'shirt_fit', 'neck', 'chest', 'waist', 'hips', 'shirt_length', 'shoulders', 'sleeve_length', 'cuff', 'arm_hole', 'biceps', 'height', 'weight']

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['address', 'phone']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserExtend(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['address', 'phone', 'gender']

