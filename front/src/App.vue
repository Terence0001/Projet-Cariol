<script setup>
  import { onMounted } from 'vue';
  import Navbar from './components/Navbar.vue';
  import Filters from './components/Filters.vue';
</script> 


<template>
  <main>
    <Navbar />

    <div class="container">
      <Filters />
    </div>

  </main>
</template>  