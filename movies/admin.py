from django.contrib import admin
from movies.models import *
# Register your models here.

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Profile)
admin.site.register(Country)