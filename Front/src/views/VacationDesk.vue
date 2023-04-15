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

import VacantionsList from "@/components/Vacations/VacantionsList.vue";


import NavBar from "@/App";
import vacantionOffer from "@/components/Vacations/vacantionOffer";
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