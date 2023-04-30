import { mapState } from 'pinia'
import useUserStore from '@/stores/users'
import ProfileMenu from '../components/NavBar/ProfileMenu.vue'
export default {
    components:{
        ProfileMenu,  
    },
  data() {
    return {
      menu: [
        { name: 'Мой профиль', link: '/profile' },
        { name: 'Менторство', link: '/profile' },
        { name: 'Настройки', link: '/profile' },
        { name: 'Выход', link: '/profile' },
      ],
      showMenu:false,
    }
  },
  computed: {
    ...mapState(useUserStore, ['getName'])
  }
}