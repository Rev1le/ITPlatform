<template>
   
    <input type="text" :placeholder="'Поиск ' + holder">
  
</template>

<script>
export default {
    props:{
        holder:{type: String,
        default:''}
    }
}
</script>

<style scoped>
input{
    border:none;
    padding: 10px;
    border-bottom: 2px solid gray;
    outline: none;
    border-radius: 10px 10px 0 0;
    width: 20%;
    font-size: 17px;
}
</style>