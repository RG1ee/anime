from rest_framework import viewsets
from apps.manga.api.serializers import MangaSerializer

from apps.manga.models import Manga


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
