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
const ordering = ref('')

const loadTasks = async () => {
  try {
    const params = new URLSearchParams()
    if (filterStatus.value !== '') {
      params.append('is_completed', filterStatus.value)
    }
    if (ordering.value !== '') {
      params.append('ordering', ordering.value)
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

<template>
  <div class="app-container">
    <h1 class="app-title">Список задач</h1>

    <TaskForm
      :editingTask="editingTask"
      @created="loadTasks"
      @updated="loadTasks"
    />

    <TaskList
      :tasks="tasks"
      @edit="setEditingTask"
      @deleted="loadTasks"
      @updated="loadTasks"
    />

    <div class="controls">
      <select v-model="filterStatus" @change="loadTasks" class="select-filter">
        <option value="">Все</option>
        <option value="true">Выполненные</option>
        <option value="false">Невыполненные</option>
      </select>

      <select v-model="ordering" @change="loadTasks" class="select-filter">
        <option disabled value="">Сортировка</option>
        <option value="created_at">По дате (старые)</option>
        <option value="-created_at">По дате (новые)</option>
      </select>
    </div>

    <div class="pagination">
      <button @click="changePage(prev)" :disabled="!prev" class="btn" :class="{ disabled: !prev }">
        Назад
      </button>
      <button @click="changePage(next)" :disabled="!next" class="btn" :class="{ disabled: !next }">
        Вперёд
      </button>
    </div>
  </div>
</template>
