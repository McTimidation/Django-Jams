from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('artist', on_delete=models.PROTECT, blank=True, null=True)
    album = models.ForeignKey('album', related_name='songs', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=50)
    fans = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=75)
    release_date = models.DateField(null=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=75)
    songs = models.ManyToManyField('Song')

    def __str__(self):
        return self.name





