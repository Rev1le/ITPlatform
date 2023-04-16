<template>
  <div class="wrap-page">
    <!-- <div class="vacations-search">  -->
      
      <InputSearch :value="searchQuery"
      @update:value="setSearchQuery" ></InputSearch>
    <!-- </div> -->
    <div class="vacation_desk">
      <VacantionsList :vacations="sortedAndSearchedVacantions" />
    </div>
  </div>
</template>

<script>
import VacantionsList from "@/components/Vacations/VacantionsList.vue";
import InputSearch from "@/components/InputSearch.vue";
import {mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
  name: "Vacation",
  components: { VacantionsList, InputSearch },
  methods: {
    ...mapMutations({

      setSearchQuery: "vacantionStore/setSearchQuery",

    }),
    ...mapActions({
      reqVacantions: "vacantionStore/reqVacantions",

    }),
  },
  mounted() {
    this.reqVacantions();
  },
  computed: {
    ...mapState({
      searchQuery: (state) => state.vacantionStore.searchQuery,
    }),
    ...mapGetters({
      // sortReports: "vacantionStore/sortReports",
      sortedAndSearchedVacantions: "vacantionStore/sortedAndSearchedVacantions",
    }),
  },
};
</script>

<style scoped>


</style>
