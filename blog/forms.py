from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "a" in title:
    #         raise forms.ValidationError("Please input a Title")
    #     else:
    #         return title

    # def clean_text(self, *args, **kwargs):
    #     text = self.cleaned_data.get("text")
    #     if text == None or text == '':
    #         raise forms.ValidationError("Please input some text")
    #     else:
    #         return text
