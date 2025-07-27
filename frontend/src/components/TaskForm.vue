<template>
  <form @submit.prevent="submitTask" class="task-form">
    <div>
      <label for="title">Заголовок</label>
      <input id="title" v-model="title" required />
    </div>
    <div>
      <label for="description">Описание</label>
      <textarea id="description" v-model="description"></textarea>
    </div>
    <button type="submit">Создать задачу</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const title = ref('')
const description = ref('')

const submitTask = async () => {
  try {
    await axios.post('http://localhost:8000/api/tasks/', {
      title: title.value,
      description: description.value
    })
    alert('Задача создана!')
    title.value = ''
    description.value = ''
  } catch (err) {
    alert('Ошибка при создании задачи.')
    console.error(err)
  }
}
</script>

<style scoped>
.task-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 400px;
}
</style>
