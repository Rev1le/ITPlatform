<template>
    <FormInput>
        <h1>Вход</h1>
        <p class="errors" v-if="errors.length">
            Пожалуйста, выполните следующие требования:
            <ul >
            <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
        </p>
        <input class="input-form" type="text" placeholder="Электронная почта" v-model="SignUp.email">
        <input class="input-form" type="password" placeholder="Пароль" v-model="SignUp.password">
        <button class="button-form" @click="toParent"> Войти </button>
    </FormInput>
</template>

<script>

import FormInput from './FormInput'

export default {
    components:{
        FormInput,
    },
    data(){
        return{
            SignUp:{
                "email":"",
                "password":""
            },
            errors:[],
        }
    },
    methods: {
        toParent(){
            if(this.SignUp.email && this.SignUp.password) {
                return this.$emit("toParent", this.SignUp);
            }
            this.errors = [];

            if(!this.SignUp.email) this.errors.push("Заполните почту");
            if(!this.SignUp.password) this.errors.push("Заполните пароль");



            
        }
    },
}
</script>

<style scoped>
h1{
    font-style: normal;
font-weight: 400;
font-size: 28px;
line-height: 44px;
}
input{
    margin: 5px 0;
}



</style>