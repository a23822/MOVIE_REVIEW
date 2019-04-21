from django import forms
from .models import Score, Movie

class ScoreForm(forms.ModelForm):
    
    class Meta:
        model = Score
        fields = ['value', 'content']