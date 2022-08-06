from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from apps.compositions.api.serializers import AnimeSerializer, MangaSerializer, RanobeSerializer

from apps.compositions.api.serializers import CompositionSerializer
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
        if self.action == 'manga':
            composition = Composition.objects.get(pk=self.kwargs[self.lookup_field])
            self.queryset = composition.manga.all()
        if self.action == 'ranobe':
            composition = Composition.objects.get(pk=self.kwargs[self.lookup_field])
            self.queryset = composition.ranobe.all()
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'anime':
            self.serializer_class = AnimeSerializer
        if self.action == 'manga':
            self.serializer_class = MangaSerializer
        if self.action == 'ranobe':
            self.serializer_class = RanobeSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["GET", "POST"])
    def anime(self, request, *args, **kwargs):
        if request.method == 'GET':
            serializer = self.get_serializer(instance=self.get_queryset(), many=True)
            return Response(serializer.data)
    
        # return Response({"message": "hello"})

    @action(detail=True, methods=["GET", "POST"])
    def manga(self, request, *args, **kwargs):
        if request.method == 'GET':
            serializer = self.get_serializer(instance=self.get_queryset(), many=True)
            return Response(serializer.data)
        
        # return Response({"message": "hello"})

    @action(detail=True, methods=["GET", "POST"])
    def ranobe(self, request, *args, **kargs):
        if request.method == 'GET':
            serializer = self.get_serializer(instance=self.get_queryset(), many=True)
            return Response(serializer.data)
