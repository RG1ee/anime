from rest_framework import serializers

from src.apps.compositions.models import Composition
from src.apps.anime.models import Anime
from src.apps.manga.models import Manga
from src.apps.ranobe.models import Ranobe


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'


class RanobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranobe
        fields = '__all__'


class CompositionSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer(many=True)
    manga = MangaSerializer(many=True)
    ranobe = RanobeSerializer(many=True)

    class Meta:
        model = Composition
        fields = (
            'id', 'name', 'description', 'anime', 'manga', 'ranobe'
        )
