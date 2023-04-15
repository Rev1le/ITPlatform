<template>
    <div class="requirements_window">
      <p>Москва</p>
      <p>Формат работы</p>
      <p>Уровень: Junior,Middle</p>
      <p>Опыт работы: 1 - 3 года</p>
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
  display: flex;
  flex-direction: column;
  gap: 10px;
  background: #EAEFF6;
  border-radius: 10px;
  padding: 10% 10%;
  font-family: "SB Sans Text", sans-serif;

}
.ok_but{
  background: #FFFFFF;
  border-radius: 10px;
  display: flex;
  align-items: center;
  gap: 10px;
}
</style>