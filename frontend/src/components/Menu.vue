<template>
    <div class="menu">
            
        <div class="menu_text">
            <span class="menu_work_text">Работа для тех,<br> кто хочет</span>
            <span class="menu_work_more_text">Большего</span>
        </div>

        <slot name="menu_buttons"/>
    </div>
</template>

<script lang="js">
import MenuButtons from "@/components/Buttons/MenuButtons.vue"

export default {
    components: {
        MenuButtons
    }
}
</script>

<style scoped>
.menu_work_text{
    font-style: normal;
    font-weight: 600;
    font-size: 64px;
    line-height: 76px;
    text-align: center;
    color: #3E3D4B;
}
.menu_work_more_text{
  font-style: normal;
    font-weight: 900;
    font-size: 110px;
    line-height: 96px;
    text-align: center;
    background-image: linear-gradient(to top right,  #0188CE, #43E3B5);
    color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
}
.menu_text{
  padding: 0 var(--pad);
  margin-top:50px;
  display: flex;
  flex-direction: column;
  text-align: center;

}
@media (max-width: 960px) {
        .work-more{
          font-size: 56px;
          line-height: 60px;
        }
        .work{
          font-size: 36px;
          line-height: 40px;
        }
    }
</style>