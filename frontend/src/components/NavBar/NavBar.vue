<template>
    <div class="nav">     
        
        <div class="Navbar-vue">          
          <router-link to="/" class="nav_bar_logo">
            <img src="@/assets/sbertest.svg" alt="" />
          </router-link>

            <div v-if="width>=1100" class="navbar_btns">
                <NavBarButtons/>
            </div>
            <div v-else class="navbar_btns navbar_btns_side">
              <button @click="showSideBar">&#9776;</button>
            </div>
        </div>
        <SideBar v-model:show="sideBarShow" ></SideBar>
    </div>
</template>

<script>
import NavBarButtons from "./NavBarButtons.vue";
import SideBar from './SideBar.vue'
export default {
  components: {
    NavBarButtons,
    SideBar,
  },
  data() {
    return {
      width: window.innerWidth,
      auth: true,
      sideBarShow:false,
    };
  },
  methods: {
    updateWidth() {
      this.width = window.innerWidth;
    },
    showSideBar(){
      console.log("kekekek")
      this.sideBarShow = true;
    },
  
  },
  created() {
    window.addEventListener("resize", this.updateWidth);
  
  },

};
</script>

<style scoped>
.work{
  font-style: normal;
font-weight: 600;
font-size: 64px;
line-height: 76px;
text-align: center;
color: #3E3D4B;
}
.work-more{
  font-style: normal;
font-weight: 900;
font-size: 110px;
line-height: 96px;
text-align: center;
background-image: linear-gradient(to top right,  #0188CE, #43E3B5);
  color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
}

.nav_bar_logo {
  width: 25%;
  min-width: 220px;
}

.navbar_btns {
  display: flex;
  align-items: center;
  margin-left: auto;
}
.nav_text{
  padding: 0 var(--pad);
  margin-top:50px;
  display: flex;
  flex-direction: column;
  text-align: center;

}
.navbar_btns_side {
  margin-left: auto;
}
.navbar_btns_side button {
  font-size: 25px;
}

.Navbar-vue {
  /* position: sticky;
  width: 100vw; */
  z-index: 10;
  display: flex;
  padding: 0 var(--pad) 0 var(--pad);
  align-items: center;
  height: 100px;
  align-items: center;
  /* filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25)); */
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

@media (max-width: 960px) {
        .work-more{
          font-size: 56px;
          line-height: 60px;
        }
        .work{
          font-size: 36px;
          line-height: 40px;
        }
    }
</style>