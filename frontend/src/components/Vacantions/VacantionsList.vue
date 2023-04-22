<template>
  
  <div class="vacation-list">
    <transition-group name="vac">
      
      <VacantionOffer 
        v-for="(vac, index) in vacations" 
        :key="index" 
        :vacation="vac"/>

    </transition-group>
  </div>

</template>

<script>
import VacantionOffer from "@/components/Vacantions/VacantionOffer.vue";
export default {
  name: "VacantionsList",
  components: { VacantionOffer },
  props:{
    vacations:{
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
