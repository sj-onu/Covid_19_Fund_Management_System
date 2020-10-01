from django import forms
from .models import DonorClass

class DonorForm(forms.ModelForm):
    class Meta:
        model = DonorClass
        fields = '__all__'