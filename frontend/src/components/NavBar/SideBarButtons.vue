<template>
    <div v-if="!getName" class="navBtns">
      <button class="auth_btn" @click="$router.push('/auth')">Войти</button>
      <button class="sign_btn" @click="$router.push('/signup')">Зарегестрироваться</button>
    </div>
    <div v-else >
     <ProfileMenu :menu="menu" :show="true" :profileName="getName"></ProfileMenu>
  </div>
  </template>
  
  <script>
  import BtnMixin from '../../mixins/BtnMixin';
  export default {
      mixins:[BtnMixin]
  }
  </script>

  