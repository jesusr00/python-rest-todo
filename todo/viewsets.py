from .models import Todo
from .serializer import TodoSerializers
from rest_framework import viewsets, permissions


class TodoViewSets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = TodoSerializers
