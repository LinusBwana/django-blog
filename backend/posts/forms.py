from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    post_title = forms.CharField(
    max_length=200,
    widget=forms.TextInput(attrs={'placeholder': 'Enter your post title'})
    )
    post_content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your post content here...',
            'rows': 10
        })
    )

    class Meta:
        model = Posts
        fields = ['post_title', 'post_content']