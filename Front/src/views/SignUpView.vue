<template>
    <div class="toForm">
      <SignUpForm></SignUpForm>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
  // import HelloWorld from '@/components/HelloWorld.vue'
  import SignUpForm from '@/components/FormsValid/SignUpForm.vue'  
  export default {
    name: 'HomeView',
    components: {
      SignUpForm
    }
  }
  </script>
  
<style scoped>

</style>