from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import TodoItem, Tag
from .serializers import TodoItemSerializer, TagSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
