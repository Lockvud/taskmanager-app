from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Добро пожаловать в Task Manager API'})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        is_completed = self.request.query_params.get('is_completed')
        if is_completed in ['true', 'false']:
            queryset = queryset.filter(is_completed=(is_completed == 'true'))
        return queryset

