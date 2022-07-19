from rest_framework import viewsets

from apps.compositions.api.serializer import CompositionSerializer
from apps.compositions.models import Composition


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
