<template>
    <div class="wrap-page">
      <!-- <div class="vacations-search">  -->
        
        <InputSearch :value="searchQuery"
        @update:value="setSearchQuery" ></InputSearch>
      <!-- </div> -->
      <div class="vacation_desk">
        <MentorsList :Mentors="sortedAndSearchedMentors" />
      </div>
    </div>
  </template>
  
  <script>
//   import VacantionsList from "@/components/Vacations/VacantionsList.vue";
import MentorsList from "@/components/Mentors/MentorsList.vue";
  import InputSearch from "@/components/InputSearch.vue";
  import {mapState,  mapGetters, mapActions, mapMutations  } from "vuex";
  export default {
    name: "Vacation",
    components: { MentorsList, InputSearch },
    methods: {
      ...mapMutations({
   
        setSearchQuery: "MentorsStore/setSearchQuery",
      
      }),
      ...mapActions({
        reqVacantions: "MentorsStore/reqMentors",
        
      }),
    },
    mounted() {
        this.reqVacantions();
      },
    computed: {
      ...mapState({
        searchQuery: (state) => state.MentorsStore.searchQuery,
      }),
      ...mapGetters({
        // sortReports: "vacantionStore/sortReports",
        sortedAndSearchedMentors: "MentorsStore/sortedAndSearchedMentors",
      }),
    },
  };
  </script>
  
  <style scoped>
  
  
  </style>
  