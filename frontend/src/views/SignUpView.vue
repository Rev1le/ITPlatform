<template>
    <div class="toForm">
      <SignUpForm @submit='signUp'></SignUpForm>
    </div>
</template>
  
    <script>
    import axios from "axios";
    import SignUpForm from '@/components/FormsValid/SignUpForm.vue'  
    import useUserStore from "@/stores/users.js";
    import {mapActions} from "pinia";
  
    export default {

    name: 'SignUpView',
    components: {
        SignUpForm
    },

    methods: {

      ...mapActions(useUserStore, ["setName"]),

      async signUp(signUp_data) {
        console.log(signUp_data);

        let input_birtday = signUp_data["birthday"].split('-');
        const formattedToday = input_birtday[2] + '-' + input_birtday[1] + '-' + input_birtday[0];
        signUp_data["birthday"] = formattedToday;

        let response = await axios.post("http://localhost:8000/api/registration/user", signUp_data);
        console.log("input: ", signUp_data, "token_data",  response.data);

        //const myStorage = window.localStorage;
        //myStorage.setItem("token", response.data.token);
        //myStorage.setItem("username", response.data.name);

        this.setName(signUp_data["name"]);
        this.$router.push("/vacation")

        return response.data

      },

      // async toParent(input){

      //   let input_birtday = input["birthday"].split('-');

      //   const formattedToday = input_birtday[2] + '-' + input_birtday[1] + '-' + input_birtday[0];

      //   input["birthday"] = formattedToday;

      //   console.log("Inputtttt", input);

      //   let response = await axios.post("http://localhost:8000/api/registration/worker", input);
      //   console.log("input: ", input, "token_data",  response.data);

      //   this.setName(input["name"]);

      //   this.$router.push("/vacation")

      //   return response.data
      // },
    }
  }
  </script>
