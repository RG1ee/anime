from rest_framework import serializers

from apps.compositions.models import Composition


class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'
        # exclude = ('id',)
