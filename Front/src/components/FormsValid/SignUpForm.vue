<template>
    <FormInput>
        <h1>Регистрация</h1>
        <p class="errors" v-if="errors.length">
            Пожалуйста, выполните следующие требования:
            <ul >
            <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
        </p>
        <input class="input-form" type="text" placeholder="ФИО" v-model="SignUp.FIO" >
        <input class="input-form" type="date"  v-model="SignUp.birth">
        <input class="input-form" type="text" placeholder="Электронная почта" v-model="SignUp.mail">
        <input class="input-form" type="text" placeholder="Пароль" v-model="SignUp.pass">
        <button class="button-form" @click="toParent"> Зарегистрироваться </button>
    </FormInput>
</template>

<script>
// import { error } from 'console';
import FormInput from './FormInput'

export default {
    components:{
        FormInput,
    },
    data(){
        return{
            SignUp:{
                "FIO":"",
                "birth":"",
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
            if(!this.SignUp.FIO) this.errors.push("Заполните ФИО");
            if(!this.SignUp.birth) this.errors.push("Заполните дату рождения");
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