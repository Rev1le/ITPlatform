<template>
    <div class="toForm">
        <AuthForm @submit='auth'></AuthForm>
    </div>
</template>


<script>
    import axios from "axios";
    import { mapMutations } from "vuex";
    import AuthForm from '@/components/FormsValid/AuthForm.vue'

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
                console.log("token_data",  response.data);

                const myStorage = window.localStorage;
                myStorage.setItem("token", response.data.token);
                myStorage.setItem("username", response.data.name);

                this.setName(response.data["name"]);
                this.$router.push("/tasks");
            },

            ...mapMutations({
                setName:"userStore/setName"
            })
        }
    }
</script>
  