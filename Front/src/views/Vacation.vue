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
import VacantionsList from "@/components/VacantionsList.vue";
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