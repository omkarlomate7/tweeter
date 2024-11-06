from django import forms
from .models import Tweet



class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-200',
                'placeholder': 'What’s happening?',
                'rows': 3,
            }),
        }