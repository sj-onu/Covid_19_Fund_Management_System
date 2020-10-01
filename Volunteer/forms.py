from django import forms
from .models import VolunteerClass

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerClass
        fields = '__all__'