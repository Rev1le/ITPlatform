<template>
  <div v-if="!getName" class="navBtns">
    <button class="auth_btn" @click="$router.push('/auth')">Войти</button>
    <button class="sign_btn" @click="$router.push('/signup')">
      Зарегестрироваться
    </button>
  </div>
  <div v-else class="navBtns">
    <button class="sign_btn" @click="$router.push('/profile')">
      {{ getName }}
    </button>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  // data() {
  //   return {
  //     btnSign:[{name:"Войти", url:"/auth"},
  //       {name:"Зарегестрироваться", url:"/signup"}],
  //     btnUser:[{name:this.getName, url:"/profile"}],

  //   };
  // },
  computed: {
    ...mapGetters({
      getName: "userStore/getName",
    }),
  },
  // watch: {
  //   // whenever question changes, this function will run
  //   getName(oldVal, newVal){
  //     // this.$nextTick(() => {
  //       this.btnUser[0].name=newVal;
  //       console.log('тут форсе')
  //     // });

  //   }
  // },
};
</script>

<style scoped>
.auth_btn {
  margin: 0 60px;
  border: none;
  background: none;
  font-size: 20px;
  /* color:white; */
}
.sign_btn {
  padding: 8.5px 20px;
  border: none;
  background: linear-gradient(
    90deg,
    rgba(66, 227, 180, 1) 0%,
    rgba(0, 135, 205, 1) 100%
  );
  border-radius: 10px;
  font-size: 20px;
  color: white;
}

</style>
