from rest_framework import serializers

from apps.compositions.api.serializer import CompositionSerializer
from apps.ranobe.models import Ranobe

class RanobeSerializer(serializers.ModelSerializer):
    composition = CompositionSerializer()

    class Meta:
        model = Ranobe
        fields = '__all__'
