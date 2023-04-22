<template>
  <div class="task_frame">
    <div class="left">
      <h1>{{ task.taskName }}</h1>
      <b>{{task.taskDescription}}</b>
    </div>
    <div class="right">
      <button  class="right_but">
        Начать тест
      </button>
      <b>Не выполнено</b>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      task: {
        taskName: "Основы Python",
        taskDescription: "Основной курс python разработчика для начинающих",
        itTaskDone: Boolean
      },
    }
  },
  name: "Tasks"
}
</script>

<style scoped>
.task_frame {
  background: #FFFFFF;
  border-radius: 10px;
  padding: 5px 4%;
  display: flex;
  justify-content: space-between;
  font-family: "SB Sans Text",sans-serif;
}
.right{
  font-family: "SB Sans Text",sans-serif;
  display: flex;
  flex-direction: column;
  gap: 10%;
}
.right_but{
  background: #FAFEF4;

  font-size: 20px;
  border-radius: 5px;
}
</style>