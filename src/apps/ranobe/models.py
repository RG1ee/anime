from django.db import models


class Ranobe(models.Model):
    composition = models.ForeignKey(
        'compositions.Composition', models.CASCADE, verbose_name="Composition"
    )


class RanobeVolume(models.Model):
    name = models.CharField(max_length=120, verbose_name="Volume Name")
    ranobe = models.ForeignKey(
        Ranobe, on_delete=models.CASCADE, verbose_name="Ranobe"
    )


class RanobeChapter(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Chapter Number")
    name = models.CharField(max_length=120, verbose_name="Chapter Title")
    description = models.TextField("Chapter Description")
    volume = models.ForeignKey(
        RanobeVolume, on_delete=models.CASCADE, verbose_name="Ranobe Volume"
    )


class RanobeText(models.Model):
    text = models.TextField(verbose_name="Ranobe Text")
    translation = models.CharField(
        max_length=120, verbose_name="Translated by: "
    )
    chapter = models.ForeignKey(
        RanobeChapter, on_delete=models.CASCADE, verbose_name="Ranobe Chapter"
    )
