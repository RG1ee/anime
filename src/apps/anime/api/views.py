from rest_framework import viewsets
from django_filters import rest_framework as filter 

from apps.users.api.permissions import IsStaffOrReadOnly

from apps.anime.api.serializers import AnimeSerializer
from apps.anime.models import Anime
from apps.anime.api.services import AnimeFilter


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsStaffOrReadOnly,)
    filter_backends = (filter.DjangoFilterBackend,)
    filterset_class = AnimeFilter
