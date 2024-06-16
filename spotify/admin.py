from django.contrib import admin
from spotify.models import Album, Artist, Song

admin.site.register([Album, Artist, Song])