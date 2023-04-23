<template>
    <div class="toForm">
      <SignUpForm @submit='signUp'></SignUpForm>
    </div>
</template>
  
  <script>
  //import axios from "axios";
  import SignUpForm from '@/components/FormsValid/SignUpForm.vue'  
  
  export default {

    name: 'SignUpView',
    components: {
      SignUpForm
    },

    methods: {

      async signUp(signUp_data) {
        console.log(signUp_data)
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
