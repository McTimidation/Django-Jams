from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'playlists', PlaylistViewSet)


urlpatterns = [
    # path('songs/', ListSongs.as_view()),
    # path('songs/<str:pk>/', ListSongs.as_view()),
    path('', include(router.urls)),
]