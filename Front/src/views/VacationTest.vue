<template>
  <div class="vacation_page">
    <workRequirements/>
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
    </div>
  </div>
</template>

<script>
import StackIcon from "@/components/Vacations/StackIcon";
import workRequirements from "@/components/Vacations/workRequirements";

export default {
  data(){
    return {
      requirements: ["nim", "react", "vue", "sql"]
    }
  },
  name: "Vacation",
  components: {StackIcon, workRequirements}
}
</script>

<style scoped>
.vacation_page {
  margin: 190px 137px;
  display: flex;

}

.window_border {
  width: 1161px;
  height: 1033px;
  padding-left: 59px;
  background: #EFFCF1;
  border-radius: 10px;
  margin-left: 81px;

}

.offer_title {
  font-family: "SB Sans Display Semibold", sans-serif;
  font-style: normal;
  font-size: 48px;
  padding-top: 32px;
}

.company_Name {
  font-family: "SB Sans Display", sans-serif;
  font-size: 29.67px;
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
  font-weight: 600;
  font-size: 20px;
  line-height: 110%;
  color: rgba(0, 0, 0, 0.3);
  padding-top: 10px;


}

.offer_text {
  font-family: "SB Sans Text", sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18.3375px;
  line-height: 110%;
  color: #3E3D4B;
  padding-top: 10px;
  height: 152px;
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
  font-weight: 600;
  font-size: 30px;
  margin-bottom: 10px;
}
.list{

  font-family: 'SB Sans Text', sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;
  margin-bottom: 5px;

}
</style>