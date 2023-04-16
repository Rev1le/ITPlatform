<template>
  <div data-tauri-drag-region class="Navbar-vue">
    <img class="nav_img" src="@/assets/logo.png" alt="" />

    <div v-if="width > 600" class="navbar_btns">
      <input id="split" name="nav" type="radio" value="0" checked />
      <label @click="$router.push('signup')" class="btn" for="split"
        >Разбить файл</label
      >

      <input id="join" name="nav" type="radio" value="1" />
      <label @click="$router.push('/auth')" class="btn" for="join">
        Собрать файл</label
      >
    </div>
    <div v-else >
      <button @click="SideBar" >☰</button>
    </div>
  </div>
</template>

<script>

export default{
  data() {
    return {
      width:0,
  }
},
methods: {
    updateWidth() {
      this.width = window.innerWidth;
    
    },
    SideBar(){
      console.log("sss")
      this.$emit("showSideBar", true);

    },
  },
  created() {
    window.addEventListener("resize", this.updateWidth);
    this.updateWidth();
  },
}
</script>

<style scoped>
input[type="radio"] {
  display: none;
}
input[type="radio"]:checked + .btn {
  border-bottom: 2px solid var(--main-color);
}

.nav_img {
  width: 32px;
}

.navbar_btns {
  display: flex;
  align-items: center;
  margin-left: auto;
}

.Navbar-vue {
  z-index: 10;
  display: flex;
  padding: 0 20px 0 20px;
  align-items: center;
  height: 50px;
  align-items: center;
}

.btn {
  transition: all 0.3s ease;
  text-decoration: none;
  padding: 5px;
  border-bottom: 2px solid transparent;
  font-size: 15px;
  background: none;
  font-weight: bold;
  color: var(--main-color);
  margin-right: 15px;
  cursor: pointer;
}

@media (hover: hover) and (pointer: fine) {
  .btn:hover {
    border-bottom: 2px solid var(--main-color);
  }
}
</style>
