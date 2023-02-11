from rest_framework import viewsets
from api.models import Task
from api.serializer import TaskSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
