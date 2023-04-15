
<template>
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
      Грустный очень нудый текст зачем он нужен воот Да кто это такой ваш цсс зачем я тут сижу на хакатоне душно уши болят
    </div>
    <div class="stack_ico">
      <StackIcon stack-name="Биба"/>
      <StackIcon stack-name="SQL"/>
    </div>
  </div>
</template>

<script>

export default{
  name: "vacantionOffer",
  components: {StackIcon}
}
import StackIcon from "@/components/StackIcon";
</script>

<style scoped>
.window_border{
  width: 1152px;
  height: 362px;
  padding-left: 59px;
  background: rgba(234, 239, 246, 0.22);
  border-radius: 10px;
  margin-bottom: 30px;

}
.offer_title{
  font-family: "SB Sans Display Semibold", sans-serif;
  font-style: normal;
  font-size: 48px;
  padding-top: 32px;
}
.company_Name{
  font-family: "SB Sans Display", sans-serif;
  font-size: 29.67px;
  color: rgba(33, 160, 56, 0.8);

}
.information_string{
  display: flex;
  justify-content:space-between;
  padding-right: 650px;
  padding-top: 10px;

}
.salary{
  font-family: 'SB Sans Display', sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 110%;
  color: rgba(0, 0, 0, 0.3);
  padding-top: 10px;


}
.offer_text{
  font-family: "SB Sans Text", sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18.3375px;
  line-height: 110%;
  color: #3E3D4B;
  padding-top: 10px;
  height: 152px;
}
.stack_ico{
  display: flex;
  margin-right: 30px;

}
</style>