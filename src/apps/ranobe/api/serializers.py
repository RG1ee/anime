from rest_framework import serializers

from src.apps.compositions.models import Composition
from src.apps.ranobe.models import Ranobe, RanobeChapter, RanobeVolume


class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'


class RanobeChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RanobeChapter
        fields = (
            'id', 'number', 'name', 'description'
        )


class RanobeVolumeSerializer(serializers.ModelSerializer):
    ranobe_chapters = RanobeChapterSerializer(many=True)

    class Meta:
        model = RanobeVolume
        fields = (
            'number', 'name', 'chapter_amount', 'ranobe_chapters'
        )


class RanobeSerializer(serializers.ModelSerializer):
    composition = CompositionSerializer(read_only=True)
    ranobe_volumes = RanobeVolumeSerializer(many=True)

    class Meta:
        model = Ranobe
        fields = (
            'id', 'status', 'composition', 'volume_amount',
            'ranobe_volumes'
        )
