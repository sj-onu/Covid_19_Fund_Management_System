from django import forms
from .models import Profile , Chat

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('receiver', 'message','image' ,'file')