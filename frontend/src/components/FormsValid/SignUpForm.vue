<template>
    <FormInput>
        <h1>Регистрация</h1>
        <p class="errors" v-if="errors.length">
            Пожалуйста, выполните следующие требования:
            <ul >
            <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
        </p>

        <InputForm v-model:input_fields="inputFields"/>

        <button class="button-form" @click="toParent"> Зарегистрироваться </button>
    </FormInput>
</template>

<script>
// import { error } from 'console';
import FormInput from './FormInput'
import InputForm from '../InputForm.vue';

export default {
    components: {
        FormInput,
        InputForm
    },

    data() {
        return{
            SignUp: {
                "name":"",
                "birthday":"",
                "email":"",
                "password":""
            },
            errors:[],
            inputFields: [
            {
                type: "text",
                placeholder: "ФИО",
                value: "",
            },
            {
                type: "date",
                placeholder: "",
                value: "",
            },
            {
                type: "text",
                placeholder: "Электронная почта",
                value: "",
            },
            {
                type: "password",
                placeholder: "Пароль",
                value: "",
            }
            ]
        }
    },
    methods: {
        toParent() {

            if(this.SignUp.name && this.SignUp.birthday && this.SignUp.email && this.SignUp.password) {
                return this.$emit("toParent", this.SignUp);
            }
            this.errors = [];
            if(!this.SignUp.name) this.errors.push("Заполните ФИО");
            if(!this.SignUp.birthday) this.errors.push("Заполните дату рождения");
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