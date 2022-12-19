from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'movies/',
        views.MovieViewSet.as_view()
    ),
]