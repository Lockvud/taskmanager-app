from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.tasks.views import TaskViewSet
from backend.tasks.views import home

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
