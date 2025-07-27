<template>
  <form @submit.prevent="submitForm" class="task-form">
    <input v-model="title" placeholder="Название задачи" required />
    <textarea v-model="description" placeholder="Описание задачи"></textarea>
    <button type="submit">Создать задачу</button>
  </form>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'

const emit = defineEmits(['created', 'updated'])
const props = defineProps({
  editingTask: Object,
})

const title = ref('')
const description = ref('')
const isEditing = ref(false)

watch(() => props.editingTask, (newTask) => {
  if (newTask) {
    title.value = newTask.title
    description.value = newTask.description
    isEditing.value = true
  } else {
    resetForm()
  }
})

const resetForm = () => {
  title.value = ''
  description.value = ''
  isEditing.value = false
}

const submitForm = async () => {
  try {
    if (isEditing.value && props.editingTask?.id) {
      await axios.put(`http://localhost:8000/api/tasks/${props.editingTask.id}/`, {
        title: title.value,
        description: description.value,
      })
      emit('updated')
    } else {
      await axios.post('http://localhost:8000/api/tasks/', {
        title: title.value,
        description: description.value,
      })
      emit('created')
    }
    resetForm()
  } catch (error) {
    console.error('Ошибка при сохранении задачи:', error)
  }
}
</script>


<style scoped>
.task-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

input, textarea {
  padding: 0.5rem;
  font-size: 1rem;
  width: 100%;
}

button {
  padding: 0.5rem;
  background: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
