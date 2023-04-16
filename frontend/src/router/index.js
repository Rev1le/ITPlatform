import { createRouter, createWebHistory } from 'vue-router'
import AuthView from '../views/AuthView.vue'
import SignUpView from '../views/SignUpView.vue'
import Vacation from "@/views/VacationDesk.vue";
import VacationTest from "@/views/VacationTest";
import TasksView from "@/views/TasksView"
import Mentors from "@/views/MentorsView"
import store from '../store/index.js'
const routes = [
  {
    path: '',
    name: 'default',
    component: AuthView,
    meta: { transition: 'slide-left', auth:false },
  },
  {
    path: '/auth',
    name: 'Auth',
    component: AuthView,
    meta: { transition: 'slide-left', auth:false },
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView,
    meta: { transition: 'slide-right', auth:false },
  },
  {
    path: '/vacation',
    name: 'Vacation',
    component: Vacation,
    
    meta: { transition: 'slide-left', auth:true },
  },
  {
    path: '/mentors',
    name: 'Mentors',
    component: Mentors,
    
    meta: { transition: 'slide-left', auth:true },
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: TasksView,
    
    meta: { transition: 'slide-right', auth:true },
  },
  {
    path: '/vacationTest/:id',
    name: 'VacationTest',
    component: VacationTest,
    meta: {transition: 'slide-right', auth:true}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  if(!store._modules.root._children.userStore.state.name && to.meta.auth){
    next({name:'Auth'});
  }
  
  else{
    next();
  }

})
export default router
