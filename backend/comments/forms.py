from .models import Comments
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['your_comment']
        widgets = {
            'your_comment': forms.Textarea(attrs={
                'placeholder': 'Write your comment',
                'class': 'form-control',
                'rows': 4
            })
        }