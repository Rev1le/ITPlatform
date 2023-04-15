<template>
    <FormInput>
        <h1>Вход</h1>
        <p class="errors" v-if="errors.length">
            Пожалуйста, выполните следующие требования:
            <ul >
            <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
        </p>
        <input class="input-form" type="text" placeholder="Электронная почта" v-model="SignUp.mail">
        <input class="input-form" type="text" placeholder="Пароль" v-model="SignUp.pass">
        <button class="button-form" @click="toParent"> Зарегистрироваться </button>
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
                "mail":"",
                "pass":""
            },
            errors:[],
        }
    },
    methods: {
        toParent(){
            if(this.SignUp.FIO && this.SignUp.birth && this.SignUp.mail && this.SignUp.pass) {
                return this.$emit("toParent", this.SignUp);
            }
            this.errors = [];

            if(!this.SignUp.mail) this.errors.push("Заполните почту");
            if(!this.SignUp.pass) this.errors.push("Заполните пароль");
            
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