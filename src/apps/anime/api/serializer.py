from rest_framework import serializers
from apps.anime.models import Anime

from apps.compositions.api.serializer import CompositionSerializer


class AnimeSerializer(serializers.ModelSerializer):
    composition = CompositionSerializer()

    class Meta:
        model = Anime
        fields = '__all__'
