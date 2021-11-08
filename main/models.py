from django.db import models


class UserMovie(models.Model):
    name = models.CharField(max_length = 100, unique = False)

    def __str__(self):
        return self.name

