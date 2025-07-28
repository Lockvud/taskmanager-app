import pytest
from rest_framework.test import APIClient
from tasks.models import Task

@pytest.mark.django_db
def test_create_task_via_api():
    client = APIClient()
    response = client.post('/api/tasks/', {
        "title": "Создание через API",
        "description": "Описание",
        "is_completed": False
    }, format='json')
    assert response.status_code == 201
    assert response.data["title"] == "Создание через API"

@pytest.mark.django_db
def test_get_tasks_via_api():
    Task.objects.create(title="Задача 1", description="...", is_completed=False)
    client = APIClient()
    response = client.get('/api/tasks/')
    assert response.status_code == 200
    assert len(response.data) >= 1

@pytest.mark.django_db
def test_update_task_via_api():
    task = Task.objects.create(title="Обновить", description="...", is_completed=False)
    client = APIClient()
    response = client.put(f'/api/tasks/{task.id}/', {
        "title": "Обновлено",
        "description": "Новый текст",
        "is_completed": True
    }, format='json')
    assert response.status_code == 200
    assert response.data["title"] == "Обновлено"
    assert response.data["is_completed"] is True

@pytest.mark.django_db
def test_delete_task_via_api():
    task = Task.objects.create(title="Удалить", description="...", is_completed=False)
    client = APIClient()
    response = client.delete(f'/api/tasks/{task.id}/')
    assert response.status_code == 204
    assert Task.objects.count() == 0
