<template>
  <div class="vacations-wrap">
  <div class="vacations-search">
      <InputSearch/>
  </div>
 <div class="vacation_desk">
   <VacantionsList/>
 </div>
</div>
</template>

<script>

import VacantionsList from "@/components/Vacations/VacantionsList.vue";
import InputSearch from "@/components/InputSearch.vue"
export default {
  name: "Vacation",
  components: {VacantionsList,
    InputSearch},
}
</script>

<style scoped>
  .vacations-wrap{
    padding: 50px var(--pad) 0;
    /* display: flex; */
  }
  .vacations-wrap>div{
    margin-bottom: 30px;
  }
  .vacations-search{
    display: flex;
    justify-content: center;
  }
</style>