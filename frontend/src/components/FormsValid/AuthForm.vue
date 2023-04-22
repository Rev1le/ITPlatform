<template>
    <div class="form-wrap">
        <div class="form">
            <h1>Вход</h1>

            <InputForm v-model:input_fields="InputFields"/>

            <p class="errors" v-if="error">
                {{ error }}
            </p>

            <button class="button-form" @click="submitForm"> Войти </button>
        </div>
    </div>
</template>

<script>

    import InputForm from './InputForm.vue';

    export default {
        emits: ['submit'],
        components: {
            InputForm
        },
        data() {
            return {
                SignInData: {
                    email: "d",
                    password: "2"
                },
                error: null,
                InputFields: [
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
            submitForm() {
                console.log(this.InputFields);
                return this.$emit('submit', this.SignInData);
            },
        },
    };
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