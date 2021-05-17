from django.core import validators
from django import forms
from .models import EntryURL

class URLForm(forms.ModelForm):
    class Meta:
        model = EntryURL
        fields = ['URL']
        widgets = {
            'URL': forms.TextInput(attrs={'class':'form-control'}),
        }