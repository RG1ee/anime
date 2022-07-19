from rest_framework import viewsets

from apps.ranobe.api.serializer import RanobeSerializer
from apps.ranobe.models import Ranobe


class RanobeViewSet(viewsets.ModelViewSet):
    queryset = Ranobe.objects.all()
    serializer_class = RanobeSerializer
