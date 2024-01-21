from .models import Tasks
from .serializers import TasksSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
