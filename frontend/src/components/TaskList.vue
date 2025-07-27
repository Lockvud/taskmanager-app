<template>
  <div>
    <ul v-if="tasks.length">
      <li v-for="task in tasks" :key="task.id">
        {{ task.title }} - {{ task.status }}
      </li>
    </ul>
    <p v-else>Задачи не найдены.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../api.js';

const tasks = ref([]);

onMounted(async () => {
  const response = await api.get('tasks/');
  tasks.value = response.data;
});
</script>
