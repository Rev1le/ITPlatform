<template>
    
    <div class="menu_buttons">
        <button
                v-for="(btn, index) in btns"
                :key="index"
                @click="$router.push(btn.url)"
                :class="[this.$route.path === btn.url ? 'nav_btn_vac' : 'nav_btn']"
                >
            {{ btn.name }}
        </button>
    </div>

</template>

<script>
    export default {

        data() {
            return {
                btns: [
                    { name: "Вакансии", url: "/vacations" },
                    { name: "Задачи", url: "/tasks" },
                    { name: "Фриланс", url: "/freelance" },
                    { name: "Менторы", url: "/mentors" }
                ],
            };
        },
    }
</script>

<style scoped>
    .menu_buttons {
        padding: 2% 10%;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 5px;
    }
    .nav_btn, .nav_btn_vac {
        background: #EAEFF7;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 16px;
    }
    .nav_btn_vac{
        color:white;
        background: #42E3B4;
    }
</style>
