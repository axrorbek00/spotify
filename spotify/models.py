from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    picture = models.URLField(blank=True)  # URLField fild rasimlarni ham loyhada ham serverlarda saqlaw un

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    cover = models.URLField(blank=True)  # album rasmi

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    cover = models.URLField(blank=True)
    source = models.URLField(blank=False, null=False)  # song  urelarni saqlash un
    listened = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title
