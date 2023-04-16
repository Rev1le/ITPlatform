<template>
    <div class="toForm">
      <AuthForm @toParent='toParent'></AuthForm>
    </div>
  </template>

  
  <script>

  import axios from "axios";
  import {mapMutations} from "vuex";

  // @ is an alias to /src
    import AuthForm from '@/components/FormsValid/AuthForm.vue'  
  
  export default {
    name: 'HomeView',
    components: {
      AuthForm
    },

    methods: {
      async toParent(input){
    console.log("авторизируемся");

        let response = await axios.post("http://localhost:8000/api/auth/worker", input);
        console.log("input: ", input, "token_data",  response.data);

        this.setName(input["email"]);

        this.$router.push("/vacation");

        return response.data
      },

      ...mapMutations({
        setName:"userStore/setName"
      })
    }
  }
  
  </script>
  