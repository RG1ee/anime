from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.manga.models import Manga
from apps.manga.api.serializers import MangaSerializer


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = (IsAuthenticated,)
