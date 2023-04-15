<template>
  <div class="vacations-wrap">
  <div class="vacations-sort">

  </div>
 <div class="vacation_desk">
   <VacantionsList/>
 </div>
</div>
</template>

<script>
<<<<<<< HEAD:Front/src/views/Vacation.vue
import VacantionsList from "@/components/VacantionsList.vue";
=======
import NavBar from "@/App";
import vacantionOffer from "@/components/Vacations/vacantionOffer";
>>>>>>> 20bf943748bd31ebaca9c50bcd3992a8d4507ae8:Front/src/views/VacationDesk.vue
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