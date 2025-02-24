from django import forms
from .models import Topic, Post
from django.contrib.auth.models import User

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', )



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'text')

