<template>
  <div>
    <Navbar />
    <main class="pt-16 mt-8">
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import Navbar from "../components/Navbar.vue";
import { RouterView } from "vue-router";
</script>
