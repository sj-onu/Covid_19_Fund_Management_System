from django import forms
from .models import DonationClass

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationClass
        fields = '__all__'