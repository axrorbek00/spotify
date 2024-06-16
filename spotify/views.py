from django.shortcuts import render
from .models import Song, Album, Artist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SongSerializer, AlbumSerializer, ArtistSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework import status, filters
from django.db import transaction
from django.contrib.postgres.search import TrigramSimilarity
from spotify.models import Song


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]  # []<-filters.SearchFilter,
    ordering_fields = ['listened', "-listened"]

    # search_fields = ['title', 'album__artist__name', 'album__title']

    def get_queryset(self):
        queryset = Song.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = (Song.objects.annotate
                        (similarity=TrigramSimilarity("title", query)
                                    + TrigramSimilarity("album__artist__name", query)
                                    + TrigramSimilarity("album__title", query)
                         ).filter
                        (similarity__gt=0.4).order_by("-similarity"))

        return queryset

    @action(detail=True, methods=['POST'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with transaction.atomic():  # db ga tranzaksiya yaratadi va 1 song ni ikki kiwi 1 vaqtda ewtsa ham 2 yozladi
            song.listened += 1
            song.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = Song.objects.order_by('-listened')[:10]  # Model obyektidan foydalanish
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = AlbumSerializer(artist.album_set.all(), many=True)

        return Response(serializer.data)

# class SongAPIView(APIView):
#     def get(self, request):
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = SongSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)  # raise_exception=True qanday xato borligni aytadi -
#         if serializer.is_valid(): ga teng
#         serializer.save()
#
