from django import forms
from .models import AreaClass

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaClass
        fields = '__all__'