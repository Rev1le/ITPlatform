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
        },
        
    };

</script>
