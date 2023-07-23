from django import forms
from .models import Post

#Our form class inherits from django's ModelForm
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)