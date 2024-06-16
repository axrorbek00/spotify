from django.urls import path, include
from .views import SongViewSet, AlbumViewSet, ArtistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls))
]
