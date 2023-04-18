<template>
    
    <div class="nav">     
        
        <div class="Navbar-vue">          
            <button @click="$router.push('/')" class="nav_bar_logo">
                <img src="@/assets/sbertest.svg" alt="" />
            </button>
            
            <div v-if="width > 1100" class="navbar_btns">
                <NavBarButtons :user="{ name: 'Рома', auth: true }"> </NavBarButtons>
            </div>
      
            <div v-else class="navbar_btns_side">
                <button @click="SideBar">☰</button>
            </div>
        </div>

        <div class="nav_text" v-show="getName">
            <span class="work">Работа для тех,<br> кто хочет</span>
            <span class="work-more">Большего</span>
            <MenuButtons></MenuButtons>
        </div>
    </div>

</template>

<script>
import NavBarButtons from "./NavBarButtons";
import MenuButtons from "../Menu/MenuButtons.vue"; // Перенести в отдельный компонент
import { mapGetters } from "vuex";
export default {
  components: {
    NavBarButtons,
    MenuButtons,
  },
  data() {
    return {
      width: 0,
      auth: true,
    };
  },
  methods: {
    updateWidth() {
      this.width = window.innerWidth;
    },
    SideBar() {
      // console.log("sss");
      this.$emit("showSideBar", true);
      },
      ImgButton() {
          console.log("ЛОГО")
      }
  },
  created() {
    window.addEventListener("resize", this.updateWidth);
    this.updateWidth();
  },
  computed: {
    ...mapGetters({
      getName: "userStore/getName",
    }),
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
  font-size: 20px;
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
