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
        setRole(role) {
            this.role = role;
        },
        setName(name) {
            this.name = name;
        },
        setUser(user) {
            this.user = user;
        },
    },
});

export default useUserStore;