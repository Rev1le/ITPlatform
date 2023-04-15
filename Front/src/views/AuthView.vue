<template>
    <div class="toForm">
      <AuthForm></AuthForm>
    </div>
  </template>
  
  <script>

  import AuthForm from '@/components/FormsValid/AuthForm'
  
  export default {
    name: 'HomeView',
    components: {
      AuthForm
    }
  }
  </script>
  