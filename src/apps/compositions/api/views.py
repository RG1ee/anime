from rest_framework import views, viewsets
from rest_framework.response import Response

from apps.compositions.models import Composition
from apps.compositions.api.serializers import CompositionSerializer


class CompositionView(views.APIView):
    def get(self, request):
        return Response(data={"name": "NARUTO"}, status=200)


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
