<script setup lang="ts">
import Hartsfield from "./components/Hartsfield.vue";
</script>

<template>
  <header>
    <div class="wrapper">
      <Hartsfield msg="You did it!" />
    </div>
  </header>
</template>

<style scoped>
header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}
</style>
