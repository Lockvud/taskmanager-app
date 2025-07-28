<template>
  <div class="task-list">
    <div
      v-for="task in tasks"
      :key="task.id"
      class="task-list-item"
    >
      <h3>
        <input
          type="checkbox"
          :checked="task.is_completed"
          @change="toggleCompleted(task)"
        />
        <span :style="{ textDecoration: task.is_completed ? 'line-through' : 'none' }">
          {{ task.title }}
        </span>
      </h3>

      <p v-if="task.description">{{ task.description }}</p>
      <small>Создано: {{ formatDate(task.created_at) }}</small>

      <div class="actions">
        <button @click="$emit('edit', task)" class="edit-btn">Редактировать</button>
        <button @click="deleteTask(task.id)" class="delete-btn">Удалить</button>
      </div>
    </div>

    <p v-if="tasks.length === 0" style="text-align:center; color:#666;">Задачи отсутствуют.</p>
  </div>
</template>

<script setup>
import axios from 'axios'

const props = defineProps({ tasks: Array })
const emit = defineEmits(['edit', 'deleted', 'updated'])

const deleteTask = async (id) => {
  if (confirm('Удалить задачу?')) {
    await axios.delete(`http://localhost:8000/api/tasks/${id}/`)
    emit('deleted')
  }
}

const toggleCompleted = async (task) => {
  try {
    await axios.patch(`http://localhost:8000/api/tasks/${task.id}/`, {
      is_completed: !task.is_completed
    })
    emit('updated')
  } catch (err) {
    console.error('Ошибка при обновлении статуса:', err)
  }
}

const formatDate = (iso) =>
  iso ? new Date(iso).toLocaleString('ru-RU') : 'неизвестно'
</script>
