<template>
    <div class="form-wrap">
        <div class="form">
            <h1>Вход</h1>

            <!-- <InputForm v-model:input_fields="InputFields"/> -->

            <InputField 
                v-for="(value, index) in InputFields" 
                v-model:field="InputFields[index]"
                v-bind:key="index"
            />

            <p class="errors" v-if="error">
                {{ error }}
            </p>

            <button class="button-form" @click="submitForm"> Войти </button>
        </div>
    </div>
</template>

<script>
    import InputField from "./InputField.vue";

    export default {
        emits: ['submit'],
        components: {
            InputField
        },
        data() {
            return {
                SignInData: {
                    email: "",
                    password: ""
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
            
                this.SignInData = {
                    email: this.InputFields[0].value,
                    password: this.InputFields[1].value
                };


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