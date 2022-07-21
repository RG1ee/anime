from rest_framework import serializers

from apps.anime.models import Anime
from apps.compositions.models import Composition


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'


class CompositionSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer(many=True)
    # manga = MangaSerializer(many=True)
    # ranobe = RanobeSerializer(many=True)

    class Meta:
        model = Composition
        fields = ('id', 'name', 'description', 'image', 'anime')
