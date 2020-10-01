from django import forms
from .models import RequestClass

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestClass
        fields = '__all__'