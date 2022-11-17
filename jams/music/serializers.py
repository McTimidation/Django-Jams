from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song, Album, Artist, Playlist
from pprint import pprint as pp


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class ArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'fans']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date']



class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    album = AlbumSerializer()
    # artist = Artist.objects.get(name=Artist['name'])
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album']

    def create(self, validated_data):
        artist = validated_data.pop('artist')
        album = validated_data.pop('album')
        art_inst, created = Artist.objects.get_or_create(name=artist['name'])
        alb_inst, created = Album.objects.get_or_create(title=album['title'])
        song = Song.objects.create(**validated_data, artist=art_inst, album=alb_inst)
        return song




class PlaylistSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']