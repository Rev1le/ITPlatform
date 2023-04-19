<template>
    <div class="toForm">
        <AuthForm @toParentAuth='Auth'></AuthForm>
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
            async Auth(input) {

                console.log("авторизируемся");

                let response = await axios.post("http://127.0.0.1:8000/api/auth", input);
                console.log("token_data",  response.data);

                this.setName(response.data["name"]);
                this.$router.push("/tasks");

                return response.data
            },

            ...mapMutations({
                setName:"userStore/setName"
            })
        }
    }
</script>
  