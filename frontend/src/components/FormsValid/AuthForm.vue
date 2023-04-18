<template>
    <FormInput>
        <h1>Вход</h1>

        <input 
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
               >

        <p class="errors" v-if="error">
            {{ error }}
        </p>

        <button class="button-form" @click="Auth"> Войти </button>

    </FormInput>
</template>

<script>
    import FormInput from './FormInput'

    export default {
        components: {
            FormInput,
        },
        emits: [
            "toParentAuth"
        ],
        data() {
            return {
                SignInData: {
                    email: null,
                    password: null
                },
                error: null,
            }
        },
        methods: {
            Auth() {

                const form_email = this.SignInData.email;
                const form_password = this.SignInData.password;

                if (form_email && form_password) {
                    this.error = null;
                    return this.$emit("toParentAuth", this.SignInData);
                }

                if (!form_email && !form_password) {
                    this.error = "Заполните почту и пароль";

                } else if (!form_email) {
                    this.error = "Заполните почту";

                } else if (!form_password) {
                    this.error = "Заполните пароль";
                }
            }
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