from django.db import models

from src.apps.manga.const import TransferStatus


class Ranobe(models.Model):
    composition = models.ForeignKey(
        'compositions.Composition', models.CASCADE,
        verbose_name="Composition", related_name='ranobe'
    )
    status = models.PositiveSmallIntegerField(
        choices=TransferStatus.choices, null=True, blank=True,
        verbose_name='Transfer Status'
    )

    def __str__(self) -> str:
        return self.composition.name

    @property
    def volume_amount(self) -> int:
        """This function counts all ranobe volumes"""
        try:
            return max([volume.number for volume in self.ranobe_volumes.all()])
        except ValueError:
            return

    class Meta():
        verbose_name_plural = 'Ranobe'


class RanobeVolume(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Volume Number")
    name = models.CharField(max_length=120, verbose_name="Volume Name")
    ranobe = models.ForeignKey(
        Ranobe, on_delete=models.CASCADE, verbose_name="Ranobe",
        related_name='ranobe_volumes'
    )

    def __str__(self) -> str:
        return f"{self.composition_name}:{self.number} volume"

    @property
    def composition_name(self) -> str:
        return self.ranobe.composition.name

    @property
    def chapter_amount(self) -> int:
        """This function counts all ranobe chapters"""
        try:
            return max(
                [chapter.number for chapter in self.ranobe_chapters.all()]
            )
        except ValueError:
            return

    class Meta:
        verbose_name_plural = 'Ranobe Volume'


class RanobeChapter(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Chapter Number")
    name = models.CharField(max_length=120, verbose_name="Chapter Title")
    description = models.TextField("Chapter Description")
    volume = models.ForeignKey(
        RanobeVolume, on_delete=models.CASCADE, verbose_name="Ranobe Volume",
        related_name='ranobe_chapters'
    )

    def __str__(self) -> str:
        return f'{self.name_ranobe}:{self.number} chapter'

    @property
    def name_ranobe(self) -> str:
        return self.volume.ranobe.composition.name

    class Meta:
        verbose_name_plural = 'Ranobe Chapter'


class RanobeText(models.Model):
    text = models.TextField(verbose_name="Ranobe Text")
    translation = models.CharField(
        max_length=120, verbose_name="Translated by: "
    )
    chapter = models.ForeignKey(
        RanobeChapter, on_delete=models.CASCADE, verbose_name="Ranobe Chapter"
    )

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.chapter.volume.ranobe.composition.name

    class Meta:
        verbose_name_plural = 'Ranobe Text'
