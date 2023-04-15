<template>
  <div class="vacation_page">
    <div>
      <workRequirements/>
    </div>

    <div class="window_border">
      <p class="offer_title">
        Питон разработчик
      </p>
      <div class="information_string">
        <b class="company_Name">
          Сбер
        </b>
        <b class="salary">
          Зарплата договорная
        </b>
      </div>
      <div class="offer_text">
        Грустный очень нудый текст зачем он нужен воот Да кто это такой ваш цсс зачем я тут сижу на хакатоне душно уши
        болят ЫАЫаыа ыа ЫАЫАЫА Ы АЫАЫАЫАЫАЫАЫаааааа ЫЫЫЫЫЫЫЫ ааа ВЫаываыаук ывацуыуавыавыавыцу куцу ц
      </div>
      <div class="stack_ico">
        <StackIcon stack-name="Биба"/>
        <StackIcon stack-name="SQL"/>
      </div>
      <div class="other_requirements">
        <p class="zag">Требования </p>
        <ul>
          <li v-for="(item, index) in requirements" :key="index" class="list">{{item}}</li>
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
export default {
  data(){
    return {
      requirements: ["nim", "react", "vue", "sql"]
    }
  },
  name: "Vacation",
  components: {StackIcon, workRequirements, Tasks}
}
</script>

<style scoped>
.vacation_page {
  padding: 0 10%;
  display: flex;

}

.window_border {
  padding-left: 30px;
  background: #EFFCF1;
  border-radius: 10px;

}

.offer_title {
  font-family: "SB Sans Display Semibold", sans-serif;
  font-style: normal;
  font-size: 48px;
  padding-top: 32px;
}

.company_Name {
  font-family: "SB Sans Display", sans-serif;
  font-size: 29px;
  color: rgba(33, 160, 56, 0.8);

}

.information_string {
  display: flex;
  gap: 30px;
  padding-top: 10px;

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
  padding-top: 10px;
}

.stack_ico {
  display: flex;
  margin-right: 30px;

}
.other_requirements{
  margin-top: 43px;
}
.zag{
  font-family: 'SB Sans Display', sans-serif;
  font-style: normal;
  font-size: 30px;
  margin-bottom: 10px;
}
.list{

  font-family: 'SB Sans Text', sans-serif;
  font-style: normal;
  font-size: 18px;
  margin-bottom: 5px;

}
</style>