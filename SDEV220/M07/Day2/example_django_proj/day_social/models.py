from django.conf import settings
from django.db import models
from django.utils import timezone


class Topic(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    epic_value = models.IntegerField()
    visible = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.topic} |\t{self.author} |\t{self.epic_value} |\t{self.text}'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
