from django import forms
from .models import MemberClass

class MemberForm(forms.ModelForm):
    class Meta:
        model = MemberClass
        fields = '__all__'