<template>
  <div v-if="!getName" class="navBtns">
    <button class="auth_btn" @click="$router.push('/auth')">Войти</button>
    <button class="sign_btn" @click="$router.push('/signup')">Зарегестрироваться</button>
  </div>
  <div v-else >
   <ProfileMenu :menu="menu" v-model:show="showMenu" :profileName="getName"></ProfileMenu>
</div>
</template>

<script>
import BtnMixin from '../../mixins/BtnMixin';
export default {
    mixins:[BtnMixin]
}
</script>

<style scoped>
.auth_btn {
  margin: 0 60px;
  border: none;
  background: none;
  font-size: 20px;
}





</style>
