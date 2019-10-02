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
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserExtend(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserExtend, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['address'].widget.attrs['readonly'] = True
            self.fields['phone'].widget.attrs['readonly'] = True

    class Meta:
        model = UserDetails
        fields = ['address', 'phone']

