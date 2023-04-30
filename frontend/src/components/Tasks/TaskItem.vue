<template>
  <div class="task">
    <div>
      <div>
        <h3>{{ task.name }}</h3>
      </div>
      <div>
        <h2>{{ task.status }}</h2>
      </div>
    </div>
    <div class="task-fot">
      <div>
        <div class="task-difficult" :data-total-value="task.difficult">
          <div class="difficult-item" data-item-value="5">&#x2605;</div>
          <div class="difficult-item" data-item-value="4">&#x2605;</div>
          <div class="difficult-item" data-item-value="3">&#x2605;</div>
          <div class="difficult-item" data-item-value="2">&#x2605;</div>
          <div class="difficult-item" data-item-value="1">&#x2605;</div>
          <p>Сложность &nbsp;</p>
        </div>
        <div>
          {{ task.desc }}
        </div>
      </div>
      <div>
        <button v-if="!task.status.length">Начать</button>
        <button v-else-if="task.status === 'Не пройдено'">Попробовать заново</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    task: {},
  },
};
</script>

<style scoped>


.task-fot {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  flex-wrap: wrap;
}
button {
  background: white;
  border-radius: 5px;
  padding: 10px 15px;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 15px;
}
.task {
  padding: 20px;
  min-width: 370px;
  min-height: 240px;
  width: 30%;
  max-width: 500px;
  background: #42e3b4;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: white;
}

.task-difficult {
  display: inline-flex;
  flex-direction: row-reverse;
}

.difficult-item {
  color: transparent;
  visibility: hidden;
  /* display: none; */
}
.task-difficult[data-total-value="1"] .difficult-item:nth-child(n + 5),
.task-difficult[data-total-value="2"] .difficult-item:nth-child(n + 4),
.task-difficult[data-total-value="3"] .difficult-item:nth-child(n + 3),
.task-difficult[data-total-value="4"] .difficult-item:nth-child(n + 2),
.task-difficult[data-total-value="5"] .difficult-item:nth-child(n + 1) {
    /* display:block; */
    visibility: visible;
  color: white;
}

@media (max-width: 330px) {
  .task{
    min-width: 310px;
  }
}

@media (min-width: 2400px) {
  .task{
    min-width: 510px;
    font-size: 25px;
  }
}

</style>
