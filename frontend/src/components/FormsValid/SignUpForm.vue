<template>
    <div class="form-wrap">
        <div class="form">
            <h1>Регистрация</h1>
            <p class="errors" v-if="errors.length">
                Пожалуйста, выполните следующие требования:
                <ul >
                    <li v-for="error in errors" :key="error">{{ error }}</li>
                </ul>
            </p>

            <InputField 
                v-for="(inp_field, index) in inputFields" 
                v-model:field="inputFields[index]" 
                :key='index'
            />

            <button class="button-form" @click="toParent"> Зарегистрироваться </button>
        </div>
    </div>
</template>

<script>
import InputField from './InputField.vue';

export default {
    components: {
        InputField
    },
    emits: ['submit'],

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
            this.errors = [];
            console.log(this.inputFields);
            
            const singUpData = this.inputFields.map((input) => input.value);

            this.SignUp = {
                "name": singUpData[0],
                "birthday": singUpData[1],
                "email": singUpData[2],
                "password": singUpData[3]
            };

            if (!this.SignUp["name"] && !this.SignUp["birthday"] && !this.SignUp["email"] && !this.SignUp["password"]) {
                this.errors.push("Заполните все поля")
                return
            }

            this.$emit('submit', this.SignUp)

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