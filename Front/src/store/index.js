import { createStore } from 'vuex';
import {userStore} from "./userStore";
import {vacantionStore} from "./vacantionStore";
export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    userStore:userStore,
    vacantionStore:vacantionStore,
  }
})
