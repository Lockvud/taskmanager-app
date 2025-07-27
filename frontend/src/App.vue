<template>
  <main class="container">
    <h1>Список задач</h1>
    <TaskList />
  </main>
</template>

<script setup>
import TaskList from './components/TaskList.vue';
</script>

<style>
.container {
  max-width: 600px;
  margin: 2rem auto;
  font-family: sans-serif;
}
</style>
