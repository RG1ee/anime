from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.compositions.api.serializers import CompositionSerializer, AnimeSerializer
from apps.compositions.models import Composition
from apps.users.api.permissions import IsStaffOrReadOnly


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly)

    def get_queryset(self):
        if self.action == 'anime':
            composition = Composition.objects.get(pk=self.kwargs[self.lookup_field])
            self.queryset = composition.anime.all()
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'anime':
            self.serializer_class = AnimeSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["GET", "POST"])
    def anime(self, request, *args, **kwargs):
        if request.method == 'GET':
            serializer = self.get_serializer(instance=self.get_queryset(), many=True)
            return Response(serializer.data)

        return Response({"message": "hello"})
