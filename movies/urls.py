from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path(
        'movies/',
        views.MovieViewSet.as_view()
    ),
]