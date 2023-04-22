<template>
  <div class="vacation_page">
    
    <VacancyRequirements :vacancyRequirements="vacancyRequirements"/>
    
    <div class="window_border">
      
      <p class="offer_title">
        {{ vacancy.name }}
        <button @click="$router.go(-1)" >
          <img src="@/assets/close.png" alt="Назад" class="close_But"/>
        </button>
      </p>
      
      <div class="information_string">
        <b class="company_Name">{{vacancy.company}}</b>
        <b class="salary">
          <div v-if="vacancy.salary===0">
            Оплата договорная
          </div>
          <div v-else>
            {{ vacancy.salary }}
          </div>
        </b>
      </div>

      <div class="offer_text">{{vacancy.description}}</div>
      
      <div class="stack_ico">
        <StackIcon 
          v-for="(item, index) in vacancy.skills" 
          :key="index" 
          :stackName="item"
        />
      </div>

      <div class="other_requirements">
        <p class="zag">Требования </p>
        
        <ul>
          <li 
            v-for="(item, index) in vacancy.skills" 
            :key="index" 
            class="list"
          > - {{item}}</li>
        </ul>

        <p class="zag" > Задания </p>
        <!-- <Tasks/> -->
      </div>
    </div>
  </div>
</template>

<script>
import StackIcon from "@/components/Vacantions/StackIcon.vue";
import VacancyRequirements from "@/components/Vacantions/VacancyRequirements.vue";
import useVacantionStore from '@/stores/vacantions';

export default {

  name: "VacancyView",
  
  components: {StackIcon, VacancyRequirements},

  data() {
    return {
      vacancy: {},
      vacancyRequirements: {
        city: "Москва",
        work_type: "Дистанционная",
        qualification: "Middle",
        work_experience: "2 года"
      }
     }
  },

  props: {
    id: {
      type: String,
      required: true
    }
  },

  // computed: {
  //   ...mapActions(useVacantionStore, ['reqVacantionById'])
  // },
  async created() {
    console.log("Создан компонент", this.id, typeof this.id);

    const store = useVacantionStore();

    const vacancy_id = this.id.toString();

    const response = await store.reqVacantionById(vacancy_id);
    console.log("Открытая вакансия: ", response.data);
    this.vacancy = response.data;
    
  },
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