<template>
  
        <NavBar/>
    <GlobalPage/>
    
</template>

<script>
    import GlobalPage from "@/views/GlobalPage.vue";
    import NavBar from "@/components/NavBar/NavBar.vue";
    import useUserStore from "@/stores/users.js";
    import {mapActions} from 'pinia';
    
    export default {
        
        components: {
            NavBar,
            GlobalPage,
        },

        created() {
            // Если пользователь уже авторизирован
            const localStorage = window.localStorage;

            // Токен может быть устаревшим
            const token = localStorage.getItem("token");
            const username = localStorage.getItem("username");

            if (token && username) {
                this.setName(username);
            }
        },

        methods: {
            ...mapActions(useUserStore, ["setName"])
        }
        
    };

</script>
