from django_filters import rest_framework as filter
from apps.anime.models import Anime


class AnimeFilter(filter.FilterSet):
    name_anime = filter.CharFilter(
        field_name='composition__name', lookup_expr='in'
    )
    status_anime = filter.NumberFilter(
        field_name='status', lookup_expr='in'
    )

    class Meta:
        model = Anime
        fields = ("composition__name", "status",)
