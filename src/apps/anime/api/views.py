from rest_framework import viewsets
from django_filters import rest_framework as filter 

from src.apps.users.api.permissions import IsStaffOrReadOnly

from src.apps.anime.api.serializers import AnimeSerializer
from src.apps.anime.models import Anime
from src.apps.anime.api.services import AnimeFilter


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsStaffOrReadOnly,)
    filter_backends = (filter.DjangoFilterBackend,)
    filterset_class = AnimeFilter
