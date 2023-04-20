<template>
      
    <router-view v-slot = "{ Component, route }">  

        <div v-if="route.meta.viewMenu">
            
            <MenuPage>
                <template #menu_buttons>
                    <MenuButtons></MenuButtons>
                </template>
            </MenuPage>

        </div>

        <transition :name = "route.meta.transition" mode="out-in">
            <component :is = "Component" /> 
        </transition>
        
    </router-view>

</template>

<script lang="js">
import MenuButtons from "@/components/Buttons/MenuButtons.vue"
import MenuPage from "@/components/Menu.vue";
import { mapGetters } from "vuex";

export default {
    components: {
        MenuPage,
        MenuButtons
    },
    computed: {
        ...mapGetters({
            getName: "userStore/getName",
        })
    }
}
</script>

<style scoped>
    .slide-left-enter-active,
    .slide-left-leave-active,
    .slide-right-enter-active,
    .slide-right-leave-active {
        transition: all 0.4s ease-in-out;
    }

    .slide-left-enter-from,
    .slide-right-leave-to {
        transform: translateX(-60%);
        opacity: 0;
    }
    
    .slide-right-enter-from,
    .slide-left-leave-to {
        transform: translateX(60%);
        opacity: 0;
    }
</style>
