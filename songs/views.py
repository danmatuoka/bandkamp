from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        album_id = self.kwargs.get("pk")
        get_object_or_404(Album, pk=album_id)
        serializer.save(album_id=album_id)

    def get_queryset(self):
        album_id = self.kwargs.get("pk")
        get_object_or_404(Album, pk=album_id)
        return self.queryset.filter(album_id=album_id)