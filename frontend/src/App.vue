<template>
    
    <div v-if="winWidth > 1100" >
        <NavBar/>
    </div>
    <div v-else>
      <!-- <button @click="SideBar">☰</button> -->
    </div>

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

        data() {
            return {
                winWidth: window.innerWidth,
            }
        },

        created() {
            const updateWinWidth = () => this.winWidth = window.innerWidth;
            window.addEventListener("resize", updateWinWidth);

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
