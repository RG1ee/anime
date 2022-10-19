from rest_framework import serializers

from apps.compositions.models import Composition
from apps.manga.models import Manga, MangaChapter, MangaImage, MangaVolume


class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'


class MangaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaImage
        fields = (
            'id', 'number', 'image'
        )


class MangaChapterSerializer(serializers.ModelSerializer):
    manga_images = MangaImageSerializer(many=True)

    class Meta:
        model = MangaChapter
        fields = (
            'id', 'number', 'name', 'volume', 'page_amount', 'manga_images'
        )


class MangaVolumeSerializer(serializers.ModelSerializer):
    manga_chapters = MangaChapterSerializer(many=True)

    class Meta:
        model = MangaVolume
        fields = (
            'id', 'number', 'chapter_amount', 'manga_chapters'
        )


class MangaSerializer(serializers.ModelSerializer):
    composition = CompositionSerializer(read_only=True)
    manga_volumes = MangaVolumeSerializer(many=True)

    class Meta:
        model = Manga
        fields = (
            'id', 'translation', 'composition', 'volume_amount',
            'manga_volumes'
        )
