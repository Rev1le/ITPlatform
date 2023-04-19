<template>

  <div class="wrap-page">
      <InputSearch></InputSearch>
      <TaskList></TaskList> 
  </div>

</template>

<script>
import MenuPage from "@/views_beta/MenuPage.vue";
import InputSearch from "@/components/InputSearch.vue";
import TaskList from "@/components/Tasks/TaskList"

export default {
    components:{
        MenuPage,
        TaskList,
        InputSearch,
    }
}
</script>

<style scodep>

</style>