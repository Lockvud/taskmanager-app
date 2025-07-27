<template>
  <main class="container">
    <h1>Список задач</h1>
    <TaskForm @created="loadTasks" />
    <TaskList :tasks="tasks" />
  </main>
</template>

<script setup>
import TaskList from './components/TaskList.vue'
import TaskForm from './components/TaskForm.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const tasks = ref([])

const loadTasks = async () => {
  const response = await axios.get('http://localhost:8000/api/tasks/')
  tasks.value = response.data
}

onMounted(loadTasks)
</script>

<style>
.container {
  max-width: 600px;
  margin: 2rem auto;
  font-family: sans-serif;
}
</style>
