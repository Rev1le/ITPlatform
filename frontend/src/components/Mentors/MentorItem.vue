
<template>
  <div class="window_border" @click="$router.push(`/mentor/${1}`)">
    <p class="offer_title">
      
      {{ mentor.name }}
    </p>
    <div class="information_string">
      <b class="company_Name">
        Сбер
      </b>
      <b class="salary">
      
        {{ mentor.salary }}
      </b>
    </div>
    <div class="offer_text">
      {{ mentor.desription }}
   
    <!-- {{  }} -->
    </div>
    <div class="stack_icons">
 
      <StackIcon v-for="(name, index) in mentor.skills" :key="index" :stack-name="name"></StackIcon>
    </div>
  </div>
</template>

<script>
import StackIcon from "@/components/Vacantions/StackIcon.vue";
export default{
  name: "MentorItem",
  components: {StackIcon},
  
  props: {
    mentor:{
     
    }
  }
}

</script>

<style scoped>
.window_border{
  
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

  word-break: break-word;
  flex-wrap: wrap;
  align-items: center;
  padding-top: 10px;

}
.salary{

  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 110%;
  color: rgba(0, 0, 0, 0.3);
  


}
.offer_text{
  font-family: "SB Sans Text", sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18.3375px;
  line-height: 110%;
  color: #3E3D4B;
  padding-top: 10px;

}
.stack_icons{
  display: flex;
  margin:30px 30px 0 0;
  flex-wrap: wrap;

}
</style>