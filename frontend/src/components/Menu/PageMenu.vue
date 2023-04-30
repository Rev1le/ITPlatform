<template>
  <div class="menu">
    <div class="menu_text">
      <span class="menu_work_text">
        <slot name="tagline"> </slot>
      </span>
      <span class="menu_work_more_text">
        <slot name="tagline-big"> </slot>
      </span>
    </div>

    <MenuButtons></MenuButtons>
  </div>
</template>

<script lang="js">
import MenuButtons from './MenuButtons.vue';
export default {
  components:{
    MenuButtons
  }
}
</script>

<style scoped>
.menu_work_text {
  font-style: normal;
  font-weight: 600;
  font-size: var(--font-size-small);
  line-height: calc(var(--font-size-small) + 12px);
  text-align: center;
  color: #3e3d4b;
}
.menu_work_more_text {
  font-style: normal;
  font-weight: 900;
  font-size: var(--font-size-big);
  line-height: calc(var(--font-size-big) - 14px);
  text-align: center;
  background-image: linear-gradient(to top right, #0188ce, #43e3b5);
  color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
}
.menu_text {
  padding: 0 var(--pad);
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  text-align: center;
}
</style>
