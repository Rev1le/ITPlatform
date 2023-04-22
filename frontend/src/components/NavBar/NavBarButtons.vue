<template>
    
    <div v-if="!getName" class="navBtns">
        <button class="auth_btn" @click="$router.push('/auth')">
            Войти
        </button>

        <button class="sign_btn" @click="$router.push('/signup')">
            Зарегестрироваться
        </button>
    </div>

    <div v-else class="navBtns">
        <button class="sign_btn" @click="$router.push('/profile')">
            {{ getName }}
        </button>
    </div>

</template>

<script>
    import { mapState } from 'pinia';
    import useUserStore from '@/stores/users';
    
    export default {
        methods: {
            // Брать из pinia
            // getName() {
            //     return ""
            // }
        },
        computed: {
            ...mapState(useUserStore, ['getName'])
        }
    };
</script>

<style scoped>
    
    .auth_btn {
        margin: 0 60px;
        border: none;
        background: none;
        font-size: 20px;
    }

.sign_btn {
  padding: 8.5px 20px;
  border: none;
  background: linear-gradient(
    90deg,
    rgba(66, 227, 180, 1) 0%,
    rgba(0, 135, 205, 1) 100%
  );
  border-radius: 10px;
  font-size: 20px;
  color: white;
}

</style>
