<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height ">
      <v-sheet
        border
        rounded
        :height="300"
        :width="800"
        class="frosted px-8 py-6 accent-border accent-text mx-auto "
      >
        <p class="mt-3 text-h1">404</p>
        
        <p class="mt-8 text-h5 font-weight-light" >
          Page not found
        </p>
        
        <div class="mt-8">
          <router-link to="/" class="font-weight-light">Go back to the home page</router-link>
        </div>
      </v-sheet>
    </v-responsive>
  </v-container>
</template>

<script lang="ts">
  export default {
    name: 'NotFound'
  }
</script>
