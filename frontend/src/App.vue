<template>
    <NavBar/>
    <GlobalPage/>
</template>

<script>
    import GlobalPage from "@/views_beta/GlobalPage.vue";
    import NavBar from "@/components/NavBar.vue";
    
    export default {
        components: {
            NavBar,
            GlobalPage,
        }
    };

</script>
