from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.anime.api.serializer import AnimeSerializer
from apps.anime.models import Anime


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsAuthenticated,)
