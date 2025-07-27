<template>
  <h1>Список задач</h1>
  <div class="container">
    <TaskForm
      :editingTask="editingTask"
      @created="loadTasks"
      @updated="loadTasks"
    />
    <TaskList :tasks="tasks" @edit="setEditingTask" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import TaskForm from './components/TaskForm.vue'
import TaskList from './components/TaskList.vue'

const tasks = ref([])
const editingTask = ref(null)

const loadTasks = async () => {
  const res = await axios.get('http://localhost:8000/api/tasks/')
  tasks.value = res.data
  editingTask.value = null
}

const setEditingTask = (task) => {
  editingTask.value = task
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
