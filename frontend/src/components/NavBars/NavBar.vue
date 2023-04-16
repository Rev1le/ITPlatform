<template>
    <NavDeckstop @showSideBar="showSideBar"></NavDeckstop>
    <SideBar v-model:show="sideBarShow" ></SideBar>
</template>

<script>
import NavDeckstop from "./NavDeckstop";
import SideBar from "./SideBar.vue";
export default {
  components: {
    NavDeckstop,
    SideBar,
  },
  data() {
    return {
      sideBarShow: false,
    };
  },
  methods: {
    showSideBar(bool) {
      this.sideBarShow = bool;
    },
  },
};
</script>

<style></style>
