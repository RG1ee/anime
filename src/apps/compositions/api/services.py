from django_filters import rest_framework as filter
from apps.compositions.models import Composition


class CompositionNameFilter(filter.FilterSet):
    name_composition = filter.CharFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Composition
        fields = ("name",)
