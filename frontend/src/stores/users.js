import { defineStore } from 'pinia'

const useUserStore = defineStore('users', {
    state: () => ({  
        role: null,
        name: null,
        user: null, 
    }),
    getters: {
        getRole(state) {return state.role;},
        getName(state) {return state.name;},
        getUser(state) {return state.user;}
    },
    actions: {
        setRole(state, role) {
            state.role = role;
        },
        setName(state, name) {
            state.name = name;
        },
        setUser(state, user) {
            state.user = user;
        },
    },
});

export default useUserStore;