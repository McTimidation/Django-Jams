from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song, Album, Artist, Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album']
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'fans']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']
        