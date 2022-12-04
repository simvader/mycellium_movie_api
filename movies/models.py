from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    imdb = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    year = models.IntegerField()

class Director(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return User.get_full_name()