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
import { mapState } from 'pinia'
import useUserStore from '@/stores/users'
import ProfileMenu from './ProfileMenu.vue'
export default {
    components:{
        ProfileMenu,
    },
  data() {
    return {
      menu: [
        { name: 'Мой профиль', link: '/profile' },
        { name: 'Менторство', link: '/profile' },
        { name: 'Настройки', link: '/profile' },
        { name: 'Выход', link: '/profile' },
      ],
      showMenu:false,
    }
  },
  methods: {
    // Брать из pinia
    // getName() {
    //     return ""
    // }
    
  },
  computed: {
    ...mapState(useUserStore, ['getName'])
  }
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
