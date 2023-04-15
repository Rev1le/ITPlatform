<template>
  <div class="nav_btn_bottom">
    
    <button
      v-for="(btn, index) in btns"
      :key="index"
      @click="$router.push(btn.url)"
      :class="[this.$route.path === btn.url ? 'nav_btn_vac' : 'nav_btn']"
    >
      {{ btn.name }}
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      btns:[{name:"Вакансии", url:"/vacation"},
      {name:"Задачи", url:"/tasks"},
      {name:"Фриланс", url:"/freelance"},
        {name:"Менторы", url:"/mentors"}],

    };
  },
}
</script>

<style scoped>
.nav_btn_bottom{
    padding: 2% 25%;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap:5px;
}
.nav_btn, .nav_btn_vac{
    background: #EAEFF7;
border-radius: 10px;
padding: 9px 16px;
font-size: 16px;
}
.nav_btn_vac{
    color:white;
    background: #42E3B4;
}
</style>
