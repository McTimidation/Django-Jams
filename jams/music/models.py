from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField(default = 180)
    artist = models.ForeignKey('artist', on_delete=models.PROTECT)
    album = models.ForeignKey('album', on_delete=models.PROTECT)


class Artist(models.Model):
    name = models.CharField(max_length=50)
    fans = models.IntegerField()

class Album(models.Model):
    title = models.CharField(max_length=75)
    release_date = models.DateField()





