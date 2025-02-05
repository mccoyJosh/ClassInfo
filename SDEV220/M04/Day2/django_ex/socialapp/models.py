from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    epic_value = models.IntegerField()

    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.save()

    def __str__(self):
        return self.username
