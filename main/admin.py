from django.contrib import admin
from .models import UserMovie, RecommendedMovies


admin.site.register(UserMovie)
admin.site.register(RecommendedMovies)
