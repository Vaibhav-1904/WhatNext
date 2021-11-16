from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('searchMovie/', views.searchMovie, name='searchMovie'),
    path('showMovies/', views.showMovies, name='showMovies'),
]
