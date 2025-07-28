import pytest
from tasks.models import Task

@pytest.mark.django_db
def test_create_task():
    task = Task.objects.create(
        title="Тестовая задача",
        description="Описание задачи",
        is_completed=True
    )
    assert task.title == "Тестовая задача"
    assert task.description == "Описание задачи"
    assert task.is_completed is True
