from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

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
    

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)