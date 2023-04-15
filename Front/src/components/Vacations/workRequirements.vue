<template>
<div class="requirements_window">
  <p class="city_name">Москва</p>
  <p class="work_type">Формат работы</p>
  <p class="work_leve">Уровень: Junior,Middle</p>
  <p class="work_stage">Опыт работы: 1 - 3 года</p>
  <button class="ok_but">Откликнуться <img class= 'padlock_img' src="@/assets/padlock_ico.png" alt=""/></button>
</div>
</template>

<script>
export default {
  name: "workRequirements"
}

</script>

<style scoped>
.padlock_img{
  height: 10px;
  width: 10px;
}
.requirements_window{
  width: 298px;
  height: 478px;
  background: #EAEFF6;
  border-radius: 10px;
  padding-left: 25px;
  padding-right: 26px;
  padding-top: 17px;

}
.city_name{
  font-family: "SB Sans Text", sans-serif;
  font-size: 16px;
  margin-top: 19px;
}
.work_type{
  margin-top: 41px;
  font-family: "SB Sans Text", sans-serif;
  font-size: 16px;
}
.work_leve{
  font-family: "SB Sans Text", sans-serif;
  font-size: 16px;
  margin-top: 41px;

}
.work_stage{
  font-family: "SB Sans Text", sans-serif;
  font-size: 16px;
  margin-top: 41px;
}
.ok_but{
  background: #FFFFFF;
  border-radius: 10px;
  width: 216px;
  height: 46px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-top: 51px;
}
</style>