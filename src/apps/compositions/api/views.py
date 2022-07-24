from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.compositions.api.serializers import CompositionSerializer
from apps.compositions.models import Composition


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    permission_classes = (IsAuthenticated,)
