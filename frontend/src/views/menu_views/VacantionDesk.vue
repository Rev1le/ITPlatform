<template>
  <div class="wrap-page">
      <InputSearch :value="searchQuery" @update:value="setSearchQuery">
      </InputSearch>
      
      <div class="vacation_desk">
        <VacantionsList :vacations="sortedAndSearchedVacantions" />
      </div>

  </div>
</template>

<script>
import VacantionsList from "@/components/Vacantions/VacantionsList.vue";
import InputSearch from "@/components/InputSearch.vue";
import { mapWritableState, mapState, mapActions } from 'pinia';
import useVacantionStore from '@/stores/vacantions';

export default {
  name: "VacationDesk",
  
  components: { 
    VacantionsList, 
    InputSearch
  },

  mounted() {
    this.reqVacantions("Hi");
  },

  methods: {
    setSearchQuery(searchQuery) {
      this.searchQuery = searchQuery;
    },
    ...mapActions(useVacantionStore, ['reqVacantions']),
  },

  computed: {
    ...mapWritableState(useVacantionStore, ['vacantions', 'searchQuery']),
    ...mapState(useVacantionStore, ['sortedAndSearchedVacantions']),
  } 
};
</script>

<style scoped>


</style>
