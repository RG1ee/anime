from django.db import models


class Manga(models.Model):
    composition = models.ForeignKey('compositions.Composition', on_delete=models.CASCADE)


class MangaVolumes(models.Model):
    number = models.PositiveSmallIntegerField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)


class MangaChapters(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=120)
    description = models.TextField()
    volume = models.ForeignKey(MangaVolumes, on_delete=models.CASCADE)


class MangaImages(models.Model):
    number = models.PositiveSmallIntegerField()
    image = models.ImageField()
    translation = models.CharField(max_length=120)
    chapter = models.ForeignKey(MangaChapters, on_delete=models.CASCADE)
