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
      this.$emit('update:show', true);
    },
  }
}
</script>

<style>
.profile-menu {
  position: relative;
  display: flex;
  justify-content: right;
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
  transition: all 0.05s ease-in;
}

.profile-menu__item a {
  text-decoration: none;
  color: inherit;
}

.profile-menu__item:hover {
  background-color: var(--hovered);
  color: white;
}

.profile-menu-enter-active,
.profile-menu-leave-active {
  transition: all 0.3s ease;
}
.profile-menu-enter-from,
.profile-menu-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.9);
}
</style>
