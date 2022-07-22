from rest_framework import serializers

from apps.compositions.api.serializers import CompositionSerializer
from apps.manga.models import Manga

class MangaSerializer(serializers.ModelSerializer):
    composition = CompositionSerializer()

    class Meta:
        model = Manga
        fields = '__all__'
