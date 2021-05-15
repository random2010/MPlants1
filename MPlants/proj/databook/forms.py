from django import forms

from . import models

class CreateDateFrom(forms.ModelForm):
    numbers = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = models.Date
        fields = (
            'day',
            'numbers',
        )