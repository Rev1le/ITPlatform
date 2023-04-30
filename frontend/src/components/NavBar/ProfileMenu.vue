<template>
  <div class="navBtns profile-menu" @mouseenter="showMenu" @mouseleave="showMenu">
    <button class="sign_btn" @click="showMenuClick">
      {{ profileName }}
    </button>
    <transition name="profile-menu">
      <div class="profile-menu__wrap" v-show="show">
        <div v-for="item in menu" :key="item" class="profile-menu__item">
          <router-link :to="item.link">{{ item.name }}</router-link>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  emits: ['update:show'],
  props: {
    menu: Array,
    show: { required: true, type: Boolean, default: false },
    profileName: { type: String, required: true }
  },
  methods: {
    showMenu() {
      this.$emit('update:show', !this.show)
    },
    showMenuClick() {
      this.$emit('update:show', true)
    }
  }
}
</script>

<style>
.profile-menu {
  position: relative;
  display: flex;
  justify-content: center;
  padding: 10px;
}
.profile-menu__wrap {
  display: flex;
  flex-direction: column;
  align-items: left;
  border-radius: 5px;
  background-color: white;
  position: absolute;
  
  top: 100%;
  width: 100%;
  min-width: 150px;
}

.profile-menu__item:first-child {
  border-radius: 5px 5px 0 0;
}
.profile-menu__item:last-child {
  border-radius: 0 0 5px 5px;
}
.profile-menu__item {
  padding: 10px 20px;
  text-decoration: none;
  color: inherit;
  text-align: center;
  transition: all 0.05s ease-in;
}

.profile-menu__item a {
  text-decoration: none;
  color: inherit;
}
@media (hover: hover) {
  .profile-menu__item:hover {
    background: linear-gradient(90deg, rgba(66, 227, 180, 1) 0%, rgba(0, 135, 205, 1) 100%);
    color: white;
  }
}

.profile-menu-enter-active,
.profile-menu-leave-active {
  transition: all 0.3s ease;
}
.profile-menu-enter-from,
.profile-menu-leave-to {
  opacity: 0;
  transform: translateY(-30px) scaleY(0.8);
}
</style>
