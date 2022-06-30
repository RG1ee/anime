from django.db import models


class Ranobe(models.Model):
    composition = models.ForeignKey('compositions.Composition', models.CASCADE)


class RanobeVolumes(models.Model):
    name = models.CharField(max_length=120)
    ranobe = models.ForeignKey(Ranobe, on_delete=models.CASCADE)


class RanobeChapters(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=120)
    description = models.TextField()
    volume = models.ForeignKey(RanobeVolumes, on_delete=models.CASCADE)


class RanobeTexts(models.Model):
    text = models.TextField()
    translation = models.CharField(max_length=120)
    chapter = models.ForeignKey(RanobeChapters, on_delete=models.CASCADE)
