from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework import permissions

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
