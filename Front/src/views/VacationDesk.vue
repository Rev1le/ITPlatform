<template>
  <div class="vacations-wrap">
  <div class="vacations-search">
      
  </div>
 <div class="vacation_desk">
   <VacantionsList/>
 </div>
</div>
</template>

<script>
<<<<<<< HEAD
import VacantionsList from "@/components/Vacations/VacantionsList.vue.js";
=======

import VacantionsList from "@/components/VacantionsList.vue";
import NavBar from "@/App";
import vacantionOffer from "@/components/Vacations/vacantionOffer";
>>>>>>> b81f8adab9a2ed2567325e4ff027b9f314349fe6
export default {
  name: "Vacation",
  components: {VacantionsList}
}
</script>

<style scoped>
  .vacations-wrap{
    padding: 50px var(--pad) 0;
    display: flex;
  }
</style>