<template>
  <h1>Список задач</h1>
  <div class="container">
    <TaskForm
      :editingTask="editingTask"
      @created="loadTasks"
      @updated="loadTasks"
    />
    <TaskList :tasks="tasks" @edit="setEditingTask" @deleted="loadTasks" />

    <select v-model="filterStatus" @change="loadTasks">
      <option value="">Все</option>
      <option value="true">Выполненные</option>
      <option value="false">Невыполненные</option>
    </select>

    <div class="pagination">
      <button @click="changePage(prev)" :disabled="!prev">Назад</button>
      <button @click="changePage(next)" :disabled="!next">Вперёд</button>
    </div>
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
const next = ref(null)
const prev = ref(null)

const loadTasks = async () => {
  try {
    const params = new URLSearchParams()
    if (filterStatus.value !== '') {
      params.append('is_completed', filterStatus.value)
    }

    const res = await axios.get(`http://localhost:8000/api/tasks/?${params.toString()}`)
    tasks.value = res.data.results
    next.value = res.data.next
    prev.value = res.data.previous
    editingTask.value = null
  } catch (err) {
    console.error('Ошибка при загрузке задач:', err)
  }
}

const changePage = async (url) => {
  if (!url) return
  try {
    const res = await axios.get(url)
    tasks.value = res.data.results
    next.value = res.data.next
    prev.value = res.data.previous
  } catch (err) {
    console.error('Ошибка при переключении страницы:', err)
  }
}

const setEditingTask = (task) => {
  editingTask.value = task
}

onMounted(loadTasks)
</script>
