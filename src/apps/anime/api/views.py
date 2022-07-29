from rest_framework import viewsets
from apps.users.api.permissions import IsStaffOrReadOnly

from apps.anime.api.serializers import AnimeSerializer
from apps.anime.models import Anime


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsStaffOrReadOnly,)
