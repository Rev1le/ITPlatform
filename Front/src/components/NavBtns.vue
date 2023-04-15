<template>
<!--  <div v-if="auth">-->
  <button v-for="(btn, index) in btnAuth" :key="index"
          >
    {{btn.name}}
  </button>
<!--</div>-->
</template>

<script>

export default {
  props: {
    auth: {
      type: Boolean,
      default: false,
    },
  },  data() {
    return {
      btnAuth:[{name:"Вакансии", url:"/vacancy"},
        {name:"Фриланс", url:"/freelance"},
        {name:"База заданий", url:"/tasks"},
        {name:"Менторы", url:"/mentors"}],
      btnSign:[{name:"Вход", url:"/auth"},
        {name:"Регистрация",url:"/signup"}],
      // sideBarShow: false,
    };
  },
  // methods: {
  //   showSideBar(bool) {
  //     this.sideBarShow = bool;
  //   },
  // },
};
</script>

<style scoped>
.auth_btn {
  margin-right: 60px;
  border: none;
  background: none;


}
.sign_btn {
  padding: 8.5px 20px;
  border: none;
  background: linear-gradient(90deg, rgba(66,227,180,1) 0%, rgba(0,135,205,1) 100%);
  border-radius: 10px;
}
</style>
