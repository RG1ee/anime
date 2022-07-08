from django.db import models
from django.core.validators import FileExtensionValidator

from apps.anime.const import AnimeStatus


class Anime(models.Model):
    composition = models.ForeignKey(
        'compositions.Composition', on_delete=models.CASCADE,
        verbose_name="Composition"
    )
    status = models.PositiveSmallIntegerField(
        choices=AnimeStatus.choices, verbose_name='anime release status',
        null=True, blank=True
    )

    def __str__(self) -> str:
        return self.composition.name

    @property
    def season_amount(self) -> int:
        try:
            return max([season.number for season in self.anime_seasons.all()])
        except ValueError:
            return

    class Meta:
        verbose_name_plural = 'Anime'


class AnimeSeason(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name="Anime Season Number"
    )
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE, verbose_name="Anime",
        related_name='anime_seasons'
    )

    def __str__(self) -> str:
        return f'{self.name}:{self.number} season'

    @property
    def name(self) -> str:
        return self.anime.composition.name

    @property
    def series_amount(self) -> int:
        try:
            return max([series.number for series in self.anime_series.all()])
        except ValueError:
            return

    class Meta:
        verbose_name_plural = 'Anime Season'


class AnimeSeries(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name="Anime Series Number"
    )
    name = models.CharField(max_length=120, verbose_name='Series Name')
    description = models.TextField(verbose_name='Description of the Series')
    season = models.ForeignKey(
        AnimeSeason, on_delete=models.CASCADE, verbose_name="Anime Season",
        related_name='anime_series'
    )

    def __str__(self) -> str:
        return f'{self.composition_name}:{self.number} series'

    @property
    def composition_name(self) -> str:
        return self.season.anime.composition.name

    class Meta:
        verbose_name_plural = 'Anime Series'


class AnimeVideo(models.Model):
    video = models.FileField(upload_to='anime', validators=[
        FileExtensionValidator(
            allowed_extensions=[
                'MOV', 'avi', 'mp4', 'webm', 'mkv'
            ]
        )
    ], verbose_name="Video")
    series = models.ForeignKey(
        AnimeSeries, on_delete=models.CASCADE, verbose_name="Anime Series"
    )

    def __str__(self) -> str:
        return self.series.season.anime.composition.name

    @property
    def name_series(self) -> str:
        return self.series.name

    class Meta:
        verbose_name_plural = 'Anime Video'
