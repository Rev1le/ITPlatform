<template>
    <div class="toForm">
      <SignUpForm @toParent='toParent'></SignUpForm>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import {mapActions, mapGetter, mapMutations} from "vuex";

  // @ is an alias to /src
  // import HelloWorld from '@/components/HelloWorld.vue'
  import SignUpForm from '@/components/FormsValid/SignUpForm.vue'  
  export default {

    name: 'HomeView',
    components: {
      SignUpForm
    },

    methods: {
      async toParent(input){

        let input_birtday = input["birthday"].split('-');

        const formattedToday = input_birtday[2] + '-' + input_birtday[1] + '-' + input_birtday[0];

        input["birthday"] = formattedToday;

        console.log("Inputtttt", input);

        let response = await axios.post("http://localhost:8000/api/registration/worker", input);
        console.log("input: ", input, "token_data",  response.data);

        this.setName(input["name"]);

        this.$router.push("/vacation")

        return response.data
      },

      ...mapMutations({
        setName:"userStore/setName"
      })
    }
  }
  </script>
  
<style scoped>

</style>