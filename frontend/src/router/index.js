import { createRouter, createWebHashHistory } from 'vue-router';
import useUserStore from '@/stores/users';

import AuthView from '../views/AuthView.vue';
//import SignUpView from '../views/menu_views/SignUpView.vue'
import VacationDesk from "../views/menu_views/VacantionDesk.vue";
//import VacationTest from "../views/menu_views/VacationTest.vue";
import TasksView from "../views/menu_views/TasksView.vue";
import Mentors from "../views/menu_views/MentorsView.vue";
import MainPage from "../views/menu_views/MainPage.vue";
import VacancyView from "../views/VacancyView.vue";


const routes = [
  {
    path: '/',
    name: 'Home',
    component: MainPage,
    meta: { transition: 'slide-left', requiresAuth: false, viewMenu: false },
  },
  {
    path: '/auth',
    name: 'Auth',
    component: AuthView,
    meta: { transition: 'slide-left', requiresAuth: false, viewMenu: false  },
  },
  // {
  //   path: '/signup',
  //   name: 'SignUp',
  //   component: () => import('../views/SignUpView.vue'),
  //   meta: { transition: 'slide-right', requiresAuth: false, viewMenu: false  },
  // },
  {
    path: '/vacations',
    name: 'Vacations',
    component: VacationDesk,
    meta: { transition: 'slide-left', requiresAuth: true, viewMenu: true  },
  },
  {
    path: '/mentors',
    name: 'Mentors',
    component: Mentors,
    meta: { transition: 'slide-left', requiresAuth: true, viewMenu: true },
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: TasksView,
    meta: { transition: 'slide-right', requiresAuth: true, viewMenu: true },
  },
  {
    path: '/vacancy/:id',
    name: 'Vacancy',
    props: true,
    component: VacancyView,
    meta: { transition: 'slide-right', requiresAuth: true, viewMenu: true },
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

router.beforeEach(async (to, from, next) => {

    const store = useUserStore();
   
    if (!store.name && to.meta.requiresAuth) {
        next({ name: 'Auth' });
    }
    else {
        next();
    }
});

export default router;
