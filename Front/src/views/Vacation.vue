<template>
 <div class="vacation_desk">
   <vacantionOffer/>
   <vacantion-offer/>
   <vacantion-offer/>
 </div>
</template>

<script>
import NavBar from "@/App";
import vacantionOffer from "@/components/vacantionOffer";
export default {
  name: "Vacation",
  components: {NavBar,vacantionOffer}
}
</script>

<style scoped>

</style>