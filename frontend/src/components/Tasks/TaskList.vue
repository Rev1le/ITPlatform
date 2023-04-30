<template>
  <div class="task-list">
    <TaskItem v-for="(task, index) in taskList" :key="index" :task="task"></TaskItem>
  </div>
</template>

<script>
import TaskItem from './TaskItem.vue';
export default {
    name: "TaskList",
    components:{
        TaskItem
    },
    data(){
        return {
            taskList:[
                {name:"Python", status:"Не пройдено", difficult:"1", desc:"SQL checkUP"},
                {name:"SQL", status:"Пройдено", difficult:"3", desc:"SQL checkUP"},
                {name:"JS", status:"Не пройдено", difficult:"4", desc:"SQL checkUP"},
                {name:"SQL", status:"Пройдено", difficult:"4", desc:"SQL checkUP"},
                {name:"Excel", status:"Не пройдено", difficult:"4", desc:"SQL checkUP"},
                {name:"SQL", status:"Не пройдено", difficult:"2", desc:"SQL checkUP"},
                {name:"Rust", status:"Пройдено", difficult:"4", desc:"SQL checkUP"},
                {name:"SQL", status:"", difficult:"4", desc:"SQL checkUP"},
                {name:"SQL", status:"Не пройдено", difficult:"4", desc:"SQL checkUP"},
                {name:"Nim", status:"Пройдено", difficult:"3", desc:"SQL checkUP"},
                {name:"SQL", status:"Не пройдено", difficult:"4", desc:"SQL checkUP"},
                {name:"SQL", status:"Не пройдено", difficult:"1", desc:"SQL checkUP"},
                {name:"SQL", status:"", difficult:"4", desc:"SQL checkUP"},
                {name:"SQL", status:"Не пройдено", difficult:"4", desc:"SQL checkUP"},
                {name:"SQL", status:"Пройдено", difficult:"5", desc:"SQL checkUP"},
            ]
        }
    },
}
</script>

<style scoped>
.task-list{
    /* display: grid;
    grid-template-columns: repeat(3,minmax(370px, 1fr)); */
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    width: 100%;
    
    gap:20px;
    /* grid-auto-rows: 240px; */
    padding-bottom: 50px;
}

.task:nth-child( 3n){
    background: #FF0066;
}
.task:nth-child( 3n+1){
    background: #42e3b4;
}
.task:nth-child( 3n+2){
    background: #0087CD;;
}

</style>