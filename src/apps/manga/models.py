from django.db import models


class Manga(models.Model):
    composition = models.ForeignKey(
        'compositions.Composition', on_delete=models.CASCADE,
        verbose_name="Composition"
    )


class MangaVolume(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Volume Number")
    manga = models.ForeignKey(
        Manga, on_delete=models.CASCADE, verbose_name="Manga"
    )


class MangaChapter(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Chapter Number")
    name = models.CharField(max_length=120, verbose_name="Chapter Title")
    description = models.TextField(verbose_name="Chapter Description")
    volume = models.ForeignKey(
        MangaVolume, on_delete=models.CASCADE, verbose_name="Manga Volume"
    )


class MangaImage(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name="Page of Manga Chapter"
    )
    image = models.ImageField(verbose_name="Image")
    translation = models.CharField(
        max_length=120, verbose_name="Translated by: "
    )
    chapter = models.ForeignKey(
        MangaChapter, on_delete=models.CASCADE, verbose_name="Manga Chapter"
    )
