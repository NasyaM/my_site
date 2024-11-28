from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
           model = Feedback
           fields = ['full_name', 'email', 'text']
           widgets = {
               'text': forms.Textarea(attrs={'rows': 4}),
           }