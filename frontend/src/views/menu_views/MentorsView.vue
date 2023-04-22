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
  export default {
    name: "MentorsView",
    components: { MentorsList, InputSearch },
    methods: {
    },
    mounted() {
        this.reqVacantions();
      },
    // computed: {
    //   ...mapState({
    //     searchQuery: (state) => state.MentorsStore.searchQuery,
    //   }),
    //   ...mapGetters({
    //     // sortReports: "vacantionStore/sortReports",
    //     sortedAndSearchedMentors: "MentorsStore/sortedAndSearchedMentors",
    //   }),
    // },
  };
  </script>
  
  <style scoped>
  
  
  </style>
  