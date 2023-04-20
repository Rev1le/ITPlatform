<template>

  <div class="wrap-page">
      <InputSearch></InputSearch>
      <TaskList></TaskList> 
  </div>

</template>

<script>
import InputSearch from "@/components/InputSearch.vue";
import TaskList from "@/components/Tasks/TaskList"

export default {
    components:{
        TaskList,
        InputSearch,
    }
}
</script>

<style scodep>

</style>