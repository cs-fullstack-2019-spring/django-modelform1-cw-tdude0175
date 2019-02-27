from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = 'title','text'
        # only need to list title and text as date and such are set to be a default