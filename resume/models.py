from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Song(models.Model):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    album_thumbnail = models.ImageField(upload_to='album_thumbnails/', null=True, blank=True)
    audio_file = models.FileField(upload_to='songs/', null=True, blank=True)
    download_count = models.IntegerField(default=0)

    def __str__(self):
        return self.song_name
