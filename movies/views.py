from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

class MovieViewSet(APIView):
    """
    API endpoint to manage movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        serializer = MovieSerializer(
            Movie.objects.all(),
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)