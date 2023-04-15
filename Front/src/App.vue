<template>
  <NavBar></NavBar>
  <router-view v-slot="{ Component, route }">
    <transition :name="route.meta.transition" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
</template>
<script>
import NavBar from "@/components/NavBars/NavBar.vue";
export default {
  components: {
    NavBar,
  },
};
</script>
<style scoped>
.slide-left-enter-active,
.slide-left-leave-active,
.slide-right-enter-active,
.slide-right-leave-active {
  transition: all 0.4s ease-in-out;
}

.slide-left-enter-from,
.slide-right-leave-to {
  transform: translateX(-60%);

  opacity: 0;
}

.slide-right-enter-from,
.slide-left-leave-to {
  transform: translateX(60%);
  opacity: 0;
}
</style>
