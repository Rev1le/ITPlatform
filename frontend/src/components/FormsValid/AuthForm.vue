<template>
    <FormInput>
        <h1>Вход</h1>

        <InputForm v-model:input_fields="InputFields"/>

        <!-- <input 
               class="input-form" 
               type="text" 
               placeholder="Электронная почта" 
               v-model="SignInData.email"
               >

        <input 
               class="input-form" 
               type="password" 
               placeholder="Пароль" 
               v-model="SignInData.password"
               > -->

        <p class="errors" v-if="error">
            {{ error }}
        </p>

        <button class="button-form" @click="submitForm"> Войти </button>

    </FormInput>
</template>

<script>
    import FormInput from './FormInput'

    import InputForm from '../InputForm.vue';

    export default {
        emits: ['submit'],
        components: {
            FormInput,
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
                const email = this.SignInData.email;
                const password =  this.SignInData.password;

                // Для отладки
                return this.$emit('submit', this.SignInData);

                if (email && password) {
                    return this.$emit('submit', this.SignInData);
                }
                
                if (!email && !password) {
                    this.error = "Заполните почту и пароль";
                } else if (!email) {
                    this.error = "Заполните почту";
                } else if (!password) {
                    this.error = "Заполните пароль";
                }
            },
            test(input) {
                console.log(input);
            }
            // Auth() {

            //     const form_email = this.SignInData.email;
            //     const form_password = this.SignInData.password;

            //     if (form_email && form_password) {
            //         this.error = null;
            //         return this.$emit("toParentAuth", this.SignInData);
            //     }

            //     if (!form_email && !form_password) {
            //         this.error = "Заполните почту и пароль";

            //     } else if (!form_email) {
            //         this.error = "Заполните почту";

            //     } else if (!form_password) {
            //         this.error = "Заполните пароль";
            //     }
            // }
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
</style>