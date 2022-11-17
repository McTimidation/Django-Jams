from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PlaylistViewSet(ModelViewSet):
    pp(Song.objects.all())
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer





# Read Operation
# class ListSongs(APIView):
#     def get_object(self, pk):
#         try:
#             return Song.objects.get(pk=pk)
#         except Song.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk=None, format=None):
#         if pk:
#             data = self.get_object(pk)
#             serializer = SongSerializer(data)
#         else:
#             data = Song.objects.all()
#             serializer = SongSerializer(data, many=True)

#         return Response(serializer.data)

# # Create Operation
#     def post(self, request, format=None):
#         print('YOU SENT A POST REQUEST')
#         data = request.data
#         serializer = SongSerializer(data=data)

#         # check if data is valid
#         serializer.is_valid(raise_exception=True)

#         # save the song sent over
#         serializer.save()

#         # tell front end that save was successful
#         response = Response()

#         response.data = {
#             'message': 'Song Created Successfully',
#             'data': serializer.data,
#         }

#         return response
    
    # def put()
