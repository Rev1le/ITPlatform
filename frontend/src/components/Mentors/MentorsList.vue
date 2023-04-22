<template>
  <div class="vacation-list">
    
    <transition-group name="vac">
      <MentorItem 
        v-for="(vac, index) in mentors" 
        :key="index" 
        :mentor="vac"
      />
    </transition-group>

  </div>
</template>

<script>
import MentorItem from "./MentorItem.vue";

export default {
  name: "MentorsList",
  components: { MentorItem },
  props: {
    mentors: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.vacation-list{
  width: 100%;
  padding-bottom: 50px;
}

.vac-enter-active,
.vac-leave-active {
  transition: all 0.5s ease;
}
.vac-enter-from,
.vac-leave-to {
  opacity: 0;
  transform: translateX(-20%);
}
vac-move {
  transition: transform 0.4s;
}
</style>
