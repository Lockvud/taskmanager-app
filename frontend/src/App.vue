<template>
  <h1>Список задач</h1>
  <div class="container">
    <TaskForm
      :editingTask="editingTask"
      @created="loadTasks"
      @updated="loadTasks"
    />
    <TaskList :tasks="tasks" @edit="setEditingTask" />
    <select v-model="filterStatus" @change="loadTasks">
      <option value="">Все</option>
      <option value="true">Выполненные</option>
      <option value="false">Невыполненные</option>
    </select>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import TaskForm from './components/TaskForm.vue'
import TaskList from './components/TaskList.vue'

const tasks = ref([])
const editingTask = ref(null)
const filterStatus = ref('')

const loadTasks = async () => {
  let url = 'http://localhost:8000/api/tasks/'
  if (filterStatus.value !== '') {
    url += `?is_completed=${filterStatus.value}`
  }
  const res = await axios.get(url)
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
