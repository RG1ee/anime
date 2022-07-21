from rest_framework import serializers

from apps.anime.models import Anime, AnimeSeason
from apps.compositions.models import Composition


class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'


class AnimeSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeSeason
        fields = ('id', 'number', 'series_amount')


class AnimeSerializer(serializers.ModelSerializer):
    composition = CompositionSerializer(read_only=True)
    anime_seasons = AnimeSeasonSerializer(many=True)

    class Meta:
        model = Anime
        fields = (
            'id', 'status', 'composition',
            'season_amount', 'anime_seasons'
        )
