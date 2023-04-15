import { createRouter, createWebHistory } from 'vue-router'
import AuthView from '../views/AuthView.vue'
import SignUpView from '../views/SignUpView.vue'
import Vacation from "@/views/VacationDesk.vue";
import VacationTest from "@/views/VacationTest";

const routes = [
  {
    path: '/',
    name: 'Auth',
    component: AuthView,
    meta: { transition: 'slide-left' },
  },
  {
    path: '/auth',
    name: 'Auth',
    component: AuthView,
    meta: { transition: 'slide-left' },
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView,
    meta: { transition: 'slide-right' },
  },
  {
    path: '/vacation',
    name: 'Vacation',
    component: Vacation,
    meta: { transition: 'slide-right' },
  },
  {
    path: '/vacationTest/:id',
    name: 'VacationTest',
    component: VacationTest,
    meta: {transition: 'slide-right'}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
