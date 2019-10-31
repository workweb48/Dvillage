from django import forms
from .models import Topic
from django.contrib.auth.models import User



class Creat_form(forms.ModelForm):
    title = forms.CharField(max_length=100,label='عنوان التصميم')
    img_url = forms.URLField(max_length=100, label='عنوان التصميم')



    class Meta:
        model= Topic

        fields = ['title', 'img_url', 'board']
