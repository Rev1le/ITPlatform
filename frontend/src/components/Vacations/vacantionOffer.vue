
<template>
  <div class="window_border" @click="$router.push(`VacationTest/${vacation.id}`)">
    <p class="offer_title">
      <!-- Питон разработчик -->
      {{ vacation.name }}
    </p>
    <div class="information_string">
      <b class="company_Name">
        Сбер
      </b>
      <b class="salary">
        <!-- Зарплата договорная -->
        {{ vacation.salary }}
      </b>
    </div>
    <div class="offer_text">
      {{ vacation.desription }}
      <!-- Грустный очень нудый текст зачем он нужен воот Да кто это такой ваш цсс зачем я тут сижу на хакатоне душно уши болят -->
    {{  }}
    </div>
    <div class="stack_icons">
      <!-- <StackIcon stack-name="Биба"/>
      <StackIcon stack-name="SQL"/> -->
      <StackIcon v-for="(name, index) in vacation.skills" :key="index" :stack-name="name"></StackIcon>
    </div>
  </div>
</template>

<script>
import StackIcon from "@/components/Vacations/StackIcon";
import vacation from "@/views/Vacation";
export default{
  name: "vacantionOffer",
  components: {StackIcon},
  methods: {
    debug(){console.log(this.vacation.id)}
  },
  props: {
    vacation:{
      // name: "Питон разработчик",
      // salary: "Зарплата договорная",
      // desription: "Требуется Python-разработчик для работы в компании. Кандидат должен иметь опыт работы с языком программирования Python и знание основных библиотек и фреймворков. Основные обязанности включают разработку и поддержку программного обеспечения на Python, написание и отладку кода, тестирование и оптимизацию производительности.",
      // skills:  ["Биба", "боба", "python"],
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