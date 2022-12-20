from django.db import models
from django.contrib.auth.models import User


class Continent(models.Model):
    name = models.CharField(max_length=60)


class Country(models.Model):
    name = models.CharField(max_length=50)



class Director(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.PROTECT)

    def __str__(self):
        return self.profile.get_full_name()


class Actor(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.PROTECT)

    def __str__(self):
        return self.user.get_full_name()


class Movie(models.Model):
    imdb = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    directors = models.ManyToManyField(Director, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)

    def __str__(self):
        return f'{self.title} - {self.year}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    seen_movies = models.ManyToManyField('Movie', through= 'MovieProfile')

    def __str__(self):
        return self.user.get_full_name()

class MovieProfile(models.Model):
    profile = models.ForeignKey(Profile, models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
