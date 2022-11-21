from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters import rest_framework as filter

from src.apps.manga.models import Manga
from src.apps.manga.api.serializers import MangaSerializer
from src.apps.manga.api.services import MangaFilter


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filter.DjangoFilterBackend,)
    filter_class = MangaFilter
