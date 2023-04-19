<template>
  <MenuPage>
  <div class="vacations-wrap">
      <div class="vacation_desk">
        <VacantionsList />
      </div>
  </div>
</MenuPage>
</template>

<script>
import VacantionsList from "@/components/Vacations/VacantionsList.vue";
import InputSearch from "@/components/InputSearch.vue";
import MenuPage from "@/views_beta/MenuPage.vue";
export default {
  name: "Vacation",
  components: { 
    VacantionsList,
    InputSearch,
    MenuPage
    },
};
</script>

<style scoped>
.vacations-wrap {
  padding: 50px var(--pad) 0;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
}
.vacations-search{
  padding: 20%;
}
</style>
