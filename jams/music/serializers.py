from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song, Album, Artist


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
        fields = ['title', 'duration', 'artist', 'album']
        