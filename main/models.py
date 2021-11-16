from django.db import models


class UserMovie(models.Model):
    name = models.CharField(max_length = 100, unique = False)

    def __str__(self):
        return self.name


class RecommendedMovies(models.Model):
    title = models.CharField(max_length = 100)
    url = models.URLField(max_length = 200)

    def __str__(self):
        return self.title

