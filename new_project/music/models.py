from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=2500)

    def __str__(self):
        return self.album_title + ' -> ' + self.artist + ' -> ' + self.genre + ' -> ' + self.album_logo

class song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.song_title 
