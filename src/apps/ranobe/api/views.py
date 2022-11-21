from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.apps.ranobe.api.serializers import RanobeSerializer
from src.apps.ranobe.models import Ranobe


class RanobeViewSet(viewsets.ModelViewSet):
    queryset = Ranobe.objects.all()
    serializer_class = RanobeSerializer
    permission_classes = (IsAuthenticated,)
