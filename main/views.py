from django.shortcuts import render
from .models import UserMovie
from .mr_model import getRecommendations
from .models import RecommendedMovies

def homePage(request):
    return render(request, "main/home.html")

def searchMovie(request):

    if request.method == "POST":
        movie_name = request.POST.get('name', None)

        if movie_name != None:

            if UserMovie.objects.count() != 0:
                UserMovie.objects.all().delete()

            search_movie = UserMovie(name = movie_name)
            search_movie.save()

            if RecommendedMovies.objects.count() != 0:
                RecommendedMovies.objects.all().delete()

            getRecommendations(movie_name)

            recommended_movies = RecommendedMovies.objects.all()

    return render(request, "main/movies.html", {'recommended_movies': recommended_movies})

def showMovies(request):
    return render(request, "main/movies.html")