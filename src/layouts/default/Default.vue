<template>
  <v-app :style="{backgroundImage: `url(${atl})`}">
    <default-view />
    <default-bar />
  </v-app>
</template>

<script lang="ts" setup>
  import atl from '@/assets/atl.jpg'
  import DefaultBar from './AppBar.vue'
  import DefaultView from './View.vue'
</script>
