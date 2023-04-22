
<template>
  <div class="window_border" @click="routingToVacancy(vacation.id)">
    <p class="offer_title">
      {{ vacation.name }}
    </p>
    <div class="information_string">
      <b class="company_Name">
        {{ vacation.company }}
      </b>
      <b class="salary">
        <div v-if="vacation.salary===0">
          Оплата договорная
        </div>
        <div v-else>
          {{ vacation.salary }}
        </div>
      </b>
    </div>
    <div class="offer_text">
      {{ vacation.desription }}
    </div>

    <div class="stack_icons">
      <StackIcon v-for="(name, index) in vacation.skills" :key="index" :stack-name="name"></StackIcon>
    </div>

  </div>
</template>

<script>
import StackIcon from "@/components/Vacantions/StackIcon.vue";
//import vacation from "@/views/Vacation";

export default{
  name: "VacantionOffer",
  
  components: { StackIcon },

  methods: {
    routingToVacancy(vacancy_id) {
      this.$router.push(`vacancy/${vacancy_id}`)
    }
  },

  props: {
    vacation: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.window_border{
  /* width: 1152px; */
  /* height: 362px; */
  /* padding-left: 59px; */
  /* padding: 30px 55px; */
  padding: 2% 5%;
  background: rgba(234, 239, 246, 0.22);
  border-radius: 10px;
  margin-bottom: 30px;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);

}
.offer_title{
  font-family: "SB Sans Display Semibold", sans-serif;
  font-style: normal;
  font-size: 48px;
  padding-top: 32px;
}
.company_Name{
  /* font-family: "SB Sans Display", sans-serif; */
  font-size: 28px;
  color: rgba(33, 160, 56, 0.8);

}
.information_string{
  display: flex;
  justify-content:space-between;
  /* gap: 10px; */
  /* width: 55%; */
  /* min-width: 310px; */
  word-break: break-word;
  flex-wrap: wrap;
  align-items: center;
  padding-top: 10px;

}
.salary{
  /* font-family: 'SB Sans Display', sans-serif; */
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 110%;
  color: rgba(0, 0, 0, 0.3);
  /* padding-top: 10px; */


}
.offer_text{
  font-family: "SB Sans Text", sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18.3375px;
  line-height: 110%;
  color: #3E3D4B;
  padding-top: 10px;
  /* height: 152px; */
}
.stack_icons{
  display: flex;
  margin:30px 30px 0 0;
  flex-wrap: wrap;
  /* margin-right: 30px; */
}
</style>