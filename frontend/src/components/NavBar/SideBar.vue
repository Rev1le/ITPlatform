<template>
    <transition name="v-sidebar">
      <div class="sidebar" @click.stop="hideSideBar" v-if="show">
        <div  class="menu">
          <button id="closeSideBar" @click.stop="hideSideBar">&#10006;</button>
          <div class="menu-item">
            <SideBarButtons :show="true" :profileName="getName"></SideBarButtons>
          </div>
        </div>
      </div>
    </transition>
    <transition name="back">
      <div @click="hideSideBar" v-if="show" class="back"></div>
    </transition>
  </template>
  
  <script>
  import SideBarButtons from "./SideBarButtons.vue";
//   import NavBtns from "./NavBtns.vue";
  export default {
    name: "my-sidebar",
    components: {
    //   NavBtns,
    SideBarButtons,
    },
    props: {
      show: {
        type: Boolean,
        default: false,
      },
    },
  
    methods: {
      hideSideBar() {
        this.$emit("update:show", false);
      },
    },
  };
  </script>
  
  <style scoped>
  .back {
    position: fixed;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.4);
    width: 100%;
    top: 0;
    left: 0;
    z-index: 9;
    transition: 0.3s ease-in-out;
  }
  #closeSideBar {
    font-size: 35px;
    
    position: absolute;
   
    right: 5px;
    margin: 5px 20px 20px 50px;
  }
  .sidebar {
    position: fixed;
    height: 100vh;
    background: none;
    width: 100%;
    top: 0;
    display: flex;
    z-index: 999;
    justify-content: right;
  }
  .menu {
    background-color: white;
    width: 65%;
  }
  .menu-item {
    padding: 100px 5%;
    width: 100%;
  }
  .navBtns {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .menu-item .btn {
    width: 100%;
  }
  
  .back-enter-active,
  .back-leave-active {
    transition: opacity 0.8s;
  }
  .back-enter-from,
  .back-leave-to {
    opacity: 0;
  }
  .v-sidebar-enter-active,
  .v-sidebar-leave-active {
    transition: all 0.8s;
  }
  .v-sidebar-enter-from,
  .v-sidebar-leave-to {
    transform: translate(100%, 0px);
  }
  </style>