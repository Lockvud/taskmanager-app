<template>
  <form class="task-form" @submit.prevent="handleSubmit">
    <div>
      <label>Название</label>
      <input
        v-model="form.title"
        type="text"
        required
      />
    </div>

    <div>
      <label>Описание</label>
      <textarea
        v-model="form.description"
        rows="4"
      ></textarea>
    </div>

      <label class="checkbox-label">
      <input v-model="form.is_completed" type="checkbox" />
      Выполнено
    </label>
    

    <button type="submit">
      {{ editingTask ? 'Сохранить' : 'Создать' }}
    </button>
  </form>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'

const emit = defineEmits(['created', 'updated'])
const props = defineProps({ editingTask: Object })

const form = ref({
  title: props.editingTask?.title || '',
  description: props.editingTask?.description || '',
  is_completed: props.editingTask?.is_completed || false,
})

const resetForm = () => {
  form.value = { title: '', description: '', is_completed: false }
}

watch(
  () => props.editingTask,
  (newTask) => {
    if (newTask) {
      form.value.title = newTask.title
      form.value.description = newTask.description
      form.value.is_completed = newTask.is_completed
    } else {
      resetForm()
    }
  },
  { immediate: true }
)

const handleSubmit = async () => {
  try {
    if (props.editingTask?.id) {
      await axios.put(`http://localhost:8000/api/tasks/${props.editingTask.id}/`, form.value)
      emit('updated')
    } else {
      await axios.post('http://localhost:8000/api/tasks/', form.value)
      emit('created')
    }
    resetForm()
  } catch (error) {
    console.error('Ошибка при сохранении задачи:', error)
  }
}
</script>
