from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('artist', on_delete=models.PROTECT, blank=True, null=True)
    album = models.ForeignKey('album', on_delete=models.PROTECT, blank=True, null=True)



class Artist(models.Model):
    name = models.CharField(max_length=50)
    fans = models.IntegerField()

class Album(models.Model):
    title = models.CharField(max_length=75)
    release_date = models.DateField()

class Playlist(models.Model):
    name = models.CharField(max_length=75)
    songs = models.ManyToManyField('Song')



