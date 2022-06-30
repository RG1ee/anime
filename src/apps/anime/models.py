from django.db import models
from django.core.validators import FileExtensionValidator


class Anime(models.Model):
    composition = models.ForeignKey(
        'compositions.Composition', on_delete=models.CASCADE
    )


class AnimeSeasons(models.Model):
    number = models.PositiveSmallIntegerField()
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)


class AnimeSeries(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=120)
    description = models.TextField()
    season = models.ForeignKey(AnimeSeasons, on_delete=models.CASCADE)


class AnimeVideos(models.Model):
    video = models.FileField(upload_to='anime', validators=[
        FileExtensionValidator(
            allowed_extensions=[
                'MOV', 'avi', 'mp4', 'webm', 'mkv'
            ]
        )
    ])
    series = models.ForeignKey(AnimeSeries, on_delete=models.CASCADE)
