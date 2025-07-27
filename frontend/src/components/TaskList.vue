<template>
    <ul class="task-list">
    <li v-for="task in tasks" :key="task.id" class="task-item">
      <h3>{{ task.title }}</h3>
      <p>{{ task.description }}</p>
      <button @click="$emit('edit', task)">Редактировать</button>
      <button @click="deleteTask(task.id)">Удалить</button>
    </li>
  </ul>
</template>


<script setup>
import axios from 'axios'
const props = defineProps({ tasks: Array })
const emit = defineEmits(['deleted'])

const deleteTask = async (id) => {
  if (confirm('Удалить задачу?')) {
    await axios.delete(`http://localhost:8000/api/tasks/${id}/`)
    emit('deleted')
  }
}
defineProps({
  tasks: {
    type: Array,
    required: true,
  }
})
</script>

<style scoped>
.task-list {
  list-style: none;
  padding: 0;
}

.task-item {
  padding: 1rem;
  border: 1px solid #ccc;
  margin-bottom: 1rem;
  border-radius: 4px;
}
</style>
