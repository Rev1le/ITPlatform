<template>
    <div class="main_page">
        <!-- <div class="main_page_text">
            <span class="main_page_title_text">Платформа<br>для любых ваших</span>
            <span class="main_page_title_more_text">целей</span>
        </div> -->
       
        <div class="description_div">
            <span class="desription_text">Сегодня Сбер - это </span>
        </div>
    </div>

</template>

<script>
</script>

<style scoped>

.main_page_text {
  padding: 0 var(--pad);
  margin-top:50px;
  display: flex;
  flex-direction: column;
  text-align: center;

}
.main_page_title_text {
    font-style: normal;
    font-weight: 600;
    font-size: 64px;
    line-height: 76px;
    text-align: center;
    color: #3E3D4B;
}
.main_page_title_more_text {
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
.description_div {
    margin: 10% 50px 50px 20%
}
.desription_text {
    font-style: bold;
    font-weight: 700px;
    font-size: 40px;
    line-height: 76px;
    text-align: center;
    color: #3E3D4B;
}
</style>