<template>
  <div class="stack_ico">
    {{ stackName }}
  </div>

</template>

<script>
export default {
  props:{
    stackName: String
  },
  name: "StackIcon"
}
</script>

<style scoped>
.stack_ico{
  /* font-family: 'SB Sans Display', sans-serif; */
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  color: #000000;
  padding: 18px 32px;
  background: #FFFFFF;
  border-radius: 15px;


}
</style>