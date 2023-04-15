<template>
<div class="form-wrap">
    <div class="form">
   <slot>

   </slot>
</div>
</div>  
</template>

<script>

</script>

<style scoped>
.form-wrap{
    margin:auto;
    border-radius: 12px;
    padding: 15px;
    min-height: 50px;
    min-width: 350px;
    width: 20%;
}
.form{
    display: flex;
    flex-direction: column;
    text-align: center;
}

</style>