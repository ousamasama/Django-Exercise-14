from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=200)

class Song(models.Model):
    song_name = models.CharField(default="", max_length=100)
    owning_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)