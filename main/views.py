from django.shortcuts import render
from .models import UserMovie

def homePage(request):
    return render(request, "main/home.html")

def searchMovie(request):

    movie_name = request.POST.get('name', None)
    if movie_name != None:
        search_movie = UserMovie(name = movie_name)
        search_movie.save()

    return render(request, "main/home.html")