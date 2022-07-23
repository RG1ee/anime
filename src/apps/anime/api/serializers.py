from rest_framework import serializers

from apps.compositions.models import Composition
from apps.anime.models import AnimeSeason, AnimeVideo
from apps.anime.models import Anime
from apps.anime.models import AnimeSeries


class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'


class AnimeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeVideo
        fields = (
            'id', 'video'
        )


class AnimeSeriesSerializer(serializers.ModelSerializer):
    anime_videos = AnimeVideoSerializer(many=True)

    class Meta:
        model = AnimeSeries
        fields = (
            'id', 'number', 'name', 'description', 'anime_videos'
        )


class AnimeSeasonSerializer(serializers.ModelSerializer):
    anime_series = AnimeSeriesSerializer(many=True)

    class Meta:
        model = AnimeSeason
        fields = (
            'id', 'number', 'series_amount', 'anime_series'
        )


class AnimeSerializer(serializers.ModelSerializer):
    composition = CompositionSerializer(read_only=True)
    anime_seasons = AnimeSeasonSerializer(many=True)

    class Meta:
        model = Anime
        fields = (
            'id', 'status', 'composition',
            'season_amount', 'anime_seasons'
        )
