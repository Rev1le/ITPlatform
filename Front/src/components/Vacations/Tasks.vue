<template>
  <div class="task_frame">
    <div>
      <p>{{ task.taskName }} dasd</p>
    </div>
    <div>
      adasdasd
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      task: {
        taskName: "sdas",
        taskDescription: String,
        itTaskDone: Boolean
      },
    }
  },
  name: "Tasks"
}
</script>

<style scoped>
.task_frame {
  width: 1052px;
  height: 102px;
  background: #FFFFFF;
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
}
</style>