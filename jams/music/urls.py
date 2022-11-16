from django.urls import path, include
from .views import SongViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    # path('songs/', ListSongs.as_view()),
    # path('songs/<str:pk>/', ListSongs.as_view()),
    path('', include(router.urls)),
]