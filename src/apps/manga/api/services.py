from django_filters import rest_framework as filter

from src.apps.manga.models import Manga


class MangaFilter(filter.FilterSet):
    name_manga = filter.CharFilter(
        field_name='composition__name', lookup_expr='in'
    )
    translation = filter.NumberFilter(
        field_name='translation', lookup_expr='in'
    )

    class Meta:
        model = Manga
        fields = ("composition__name", "translation",)
