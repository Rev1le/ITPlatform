<template>
    <div class="toForm">
        <AuthForm @submit='auth'></AuthForm>
    </div>
</template>

<script>
    import axios from "axios";
    import AuthForm from '@/components/FormsValid/AuthForm.vue';
    import { mapWritableState } from 'pinia'
    import useUserStore from '@/stores/users.js';

    export default {
        name: 'HomeView',
        components: {
            AuthForm
        },
        methods: {
            async auth(sign_in_data) {

                console.log("Авторизируемся");

                // Ошибка

                let response = await axios.post("http://127.0.0.1:8000/api/auth", sign_in_data);
                //console.log("token_data",  response.data);

                const myStorage = window.localStorage;
                myStorage.setItem("token", response.data.token);
                myStorage.setItem("username", response.data.name);

                //this.setName(response.data["name"]);
                this.name = response.data["name"];
                await this.$router.push("/tasks");
            },
        },
        computed: {
            ...mapWritableState(useUserStore, ['name'])
        }
    }
</script>

<style scoped>

</style>
  