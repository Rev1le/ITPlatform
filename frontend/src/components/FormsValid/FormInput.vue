<template>
<div class="form-wrap">
    <div class="form">
        <slot/>
    </div>
</div>  
</template>

<style scoped>
.form-wrap{
    margin:auto;
    border-radius: 12px;
    padding: 15px;
    min-height: 50px;
    min-width: 200px;
    width: 40%;
}
.form{
    display: flex;
    flex-direction: column;
    text-align: center;
}

@media (max-width: 700px) {
    .form-wrap{
        width: 90%;
    }
}
</style>