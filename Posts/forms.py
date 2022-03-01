from django import forms
from .models import Post
from tinymce.widgets import TinyMCE


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_inp', 'placeholder': 'Tytuł'}), label="")
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="")

    class Meta:
        model = Post
        fields = ('title', 'content', 'thumbnail', )
