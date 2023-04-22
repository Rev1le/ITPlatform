<template>
  <div class="requirements_window">
      <p>Город: {{ vacancyRequirements.city }}</p>
      <p>Тип работы: {{ vacancyRequirements.work_type }}</p>
      <p>Квалификация: {{ vacancyRequirements.qualification }}</p>
      <p>Опыт работы: {{ vacancyRequirements.work_experience }}</p>
      <button class="ok_but">
        Откликнуться 
        <img class= 'padlock_img' src="@/assets/padlock_ico.png" alt=""/>
      </button>
  </div>
</template>

<script>
export default {
  name: "VacancyRequirements",
  props: {
    vacancyRequirements: {
      type: Object,
      required: false,
      default() {
        return {
          city: "загружается...",
          work_type: "загружается...",
          qualification: "загружается...",
          work_experience: "загружается..."
        }
      }
    }
  }
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
  justify-content: space-around;
  gap: 20px;
  background: #EAEFF6;
  border-radius: 10px;
  padding: 2% 2%;
  font-family: "SB Sans Text", sans-serif;

}
.ok_but{
  background: #FFFFFF;
  border-radius: 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 2%;
  padding: 3% 3%;
}
</style>