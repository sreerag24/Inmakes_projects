from django.contrib import admin

# Register your models here.
from .models import Movie


admin.site.register(Movie)


def __str__(self):
    return self.name

