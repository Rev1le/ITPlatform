<template>
  <div class="vacation_page">
    <workRequirements/>
    <div class="window_border">
      <p class="offer_title">
        {{ vacantion.name }}
        <button @click="$router.go(-1)" ><img src="@/assets/close.png" alt="Назад" class="close_But"/></button>
      </p>
      <div class="information_string">
        <b class="company_Name">
          {{company}}
        </b>
        <b class="salary">
          {{ vacantion.salary }}
        </b>
      </div>
      <div class="offer_text">
        {{
          vacantion.description
        }}
      </div>
      <div class="stack_ico">
        <StackIcon stack-name="Биба"/>
        <StackIcon stack-name="SQL"/>
      </div>
      <div class="other_requirements">
        <p class="zag">Требования </p>
        <ul>
          <li v-for="(item, index) in skills" :key="index" class="list"> - {{item}}</li>
        </ul>
        <p class="zag" > Задания </p>
      </div>
      <Tasks/>
    </div>
  </div>
</template>

<script>
import StackIcon from "@/components/Vacations/StackIcon";
import workRequirements from "@/components/Vacations/workRequirements";
import Tasks from "@/components/Vacations/Tasks";
import {mapActions} from "vuex";

export default {
  data(){
    return {
      vacantion: {

      },

      // company:'',
      // salary:'',
      // vacationName: '',
      // description: '',
      // skills: ["nim", "react", "vue", "sql"],
      methods: {
        ...mapActions({
          reqVacantionById: "vacantionStore/reqVacantionById",

        }),
      },
     async mounted() {
        this.vacantion = await this.reqVacantionById(this.$route.params.id)

      }
    }
  },
  name: "Vacation",
  components: {StackIcon, workRequirements, Tasks}
}
</script>

<style scoped>
.vacation_page {
  padding: 20px 10%;
  display: flex;
  flex-direction: row;
  gap: 2%;

}


.window_border {
  padding: 1% 3%;
  background: #EFFCF1;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  gap: 15px;

}

.offer_title {
  font-family: "SB Sans Display Semibold", sans-serif;
  font-style: normal;
  font-size: 48px;
  display: flex;
  justify-content: space-between;

}

.company_Name {
  font-family: "SB Sans Display", sans-serif;
  font-size: 29px;
  color: rgba(33, 160, 56, 0.8);

}

.information_string {
  display: flex;
  gap: 30px;


}

.close_But{
  height: 20px;
  width: 20px;
}

.salary {
  font-family: 'SB Sans Display', sans-serif;
  font-style: normal;
  font-size: 20px;
  color: rgba(0, 0, 0, 0.3);
  padding-top: 10px;


}

.offer_text {
  font-family: "SB Sans Text", sans-serif;
  font-style: normal;
  font-size: 18px;
  color: #3E3D4B;
}

.stack_ico {
  display: flex;
  justify-content: flex-start;
  gap: 10px;

}
.other_requirements{
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.zag{
  font-family: 'SB Sans Display', sans-serif;
  font-style: normal;
  font-size: 30px;
}
.list{
  display: flex;
  font-family: 'SB Sans Text', sans-serif;
  font-style: normal;
  font-size: 20px;


}
</style>