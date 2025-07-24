from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Добро пожаловать в Task Manager API'})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

