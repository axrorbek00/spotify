from .models import Song, Artist, Album
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = Song
        fields = '__all__'

    def validate_source(self, value):
        if not value.endswith('.mp3'):
            raise ValidationError(detail='Must be .mp3')

        return value
