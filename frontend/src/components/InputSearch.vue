<template>
   <div class="search">
    <input type="text" :placeholder="'Поиск ' + holder" :value="value" @input="updateInput">
</div> 

</template>

<script>
export default {
    props:{
        holder:{type: String,
        default:''},
        value : [String, Number],
    },
    methods:{
        updateInput(event){
            this.$emit("update:value", event.target.value)
        }
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
.search{
  padding-bottom: 50px;
  display: flex;
  justify-content: center;
}
</style>