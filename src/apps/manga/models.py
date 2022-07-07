from django.db import models


class Manga(models.Model):
    TRANSFER_STATUS = (
        (1, 'Продолжается'),
        (2, 'Заморожен'),
        (3, 'Завершен'),
        (4, 'Заброшен'),
    )
    composition = models.ForeignKey(
        'compositions.Composition', on_delete=models.CASCADE,
        verbose_name="Composition"
    )
    translation = models.PositiveSmallIntegerField(
        choices=TRANSFER_STATUS,
        verbose_name="Translated status: ", null=True, blank=True
    )

    def __str__(self) -> str:
        return self.composition.name

    @property
    def volume_amount(self):
        try:
            return max([volume.number for volume in self.manga_volumes.all()])
        except ValueError:
            return None

    class Meta():
        verbose_name_plural = 'Manga'


class MangaVolume(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Volume Number")
    manga = models.ForeignKey(
        Manga, on_delete=models.CASCADE, verbose_name="Manga",
        related_name='manga_volumes'
    )

    def __str__(self) -> str:
        return self.manga.composition.name

    @property
    def name(self) -> str:
        return (self.manga.composition.name)

    def chapter_amount(self):
        try:
            return max(
                [chapter.number for chapter in self.manga_chapters.all()]
            )
        except ValueError:
            return None

    class Meta():
        verbose_name_plural = 'Manga Volume'


class MangaChapter(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name="Chapter Number")
    name = models.CharField(max_length=120, verbose_name="Chapter Title")
    description = models.TextField(verbose_name="Chapter Description")
    volume = models.ForeignKey(
        MangaVolume, on_delete=models.CASCADE, verbose_name="Manga Volume",
        related_name='manga_chapters'
    )

    def __str__(self) -> str:
        return self.volume.manga.composition.name

    @property
    def name_manga(self) -> str:
        return self.volume.manga.composition.name

    def page_amount(self):
        try:
            return max([image.number for image in self.manga_images.all()])
        except ValueError:
            return None

    class Meta():
        verbose_name_plural = 'Manga Chapter'


class MangaImage(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name="Page of Manga Chapter"
    )
    image = models.ImageField(verbose_name="Image")
    chapter = models.ForeignKey(
        MangaChapter, on_delete=models.CASCADE, verbose_name="Manga Chapter",
        related_name='manga_images'
    )

    def chapter_name(self) -> str:
       return self.chapter.name

    @property
    def name_manga(self):
        return self.chapter.volume.manga.composition.name

    class Meta:
        verbose_name_plural = 'Mango Image'
