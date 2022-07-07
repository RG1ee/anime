from django.db import models


class Ranobe(models.Model):
    TRANSFER_STATUS = (
        (1, 'Продолжается'),
        (2, 'Заморожен'),
        (3, 'Завершен'),
        (4, 'Заброшен'),
    )
    composition = models.ForeignKey(
        'compositions.Composition', models.CASCADE, verbose_name="Composition"
    )
    status = models.PositiveSmallIntegerField(
        choices=TRANSFER_STATUS, null=True, blank=True,
        verbose_name='Transfer Status'
    )
    def __str__(self):
        return self.composition.name

    @property
    def volume_amount(self):
        try:
            return max([volume.number for volume in self.ranobe_volumes.all()])
        except ValueError:
            return None

    class Meta():
        verbose_name_plural = 'Ranobe'


class RanobeVolume(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Volume Number")
    name = models.CharField(max_length=120, verbose_name="Volume Name")
    ranobe = models.ForeignKey(
        Ranobe, on_delete=models.CASCADE, verbose_name="Ranobe",
        related_name='ranobe_volumes'
    )

    def __str__(self):
        return self.ranobe.composition.name

    @property
    def name(self):
        return self.ranobe.composition.name

    def chapter_amount(self):
        try:
            return max([chapter.number for chapter in self.ranobe_chapters.all()])
        except ValueError:
            return None

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

    def __str__(self):
        return self.volume.ranobe.composition.name

    @property
    def name_ranobe(self):
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

    def __str__(self):
        return self.chapter.volume.ranobe.composition.name

    @property
    def name(self):
        return self.chapter.volume.ranobe.composition.name

    class Meta:
        verbose_name_plural = 'Ranobe Text'
