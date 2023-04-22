<template>
    <div class="wrap-page">
        
      <InputSearch :value="searchQuery"
        @update:value="setSearchQuery" 
      />

      <div class="vacation_desk">
        <MentorsList :mentors="sortedAndSearchedMentors" />
      </div>

    </div>
  </template>
  
  <script>
  import MentorsList from "@/components/Mentors/MentorsList.vue";
  import InputSearch from "@/components/InputSearch.vue";
  import useMentorStore from "@/stores/mentors";
  import { mapActions, mapState, mapWritableState } from "pinia";


  export default {
    name: "MentorsView",
    
    components: { 
      MentorsList,
      InputSearch 
    },
    mounted() {
      this.reqMentors("Hi");
    },
    
    methods: {
      setSearchQuery(searchQuery) {
        this.searchQuery = searchQuery;
      },
      ...mapActions(useMentorStore, ["reqMentors", "reqMentorsById"]),
    },

    computed: {
      ...mapWritableState(useMentorStore, ['mentors', 'searchQuery']),
      ...mapState(useMentorStore, ["sortedAndSearchedMentors"]),
    },


  };
  </script>
  
  