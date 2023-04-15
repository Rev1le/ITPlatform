import axios from "axios";
export const userStore = {
  state: () => (
    {
    role:'', 
    name:'asdasd', 
    user:'',
  }),

  getters: {
    getRole(state){
        return state.role;
    },
    getName(state){
        return state.name;
    },
    getUser(state){
        return state.user;
    }
  },
  mutations: {
    setRole(state, role){
        state.role = role;
    },
    setName(state, name){
        state.name = name;
    },
    setUser(state, user){
        state.user = user;
    },

    setStateAll(state, userData){
        state.role = userData.role;
        state.name = userData.name;
        state.user = userData.user;
    }
  },
  actions: {
    async entrance({commit}, entr){
        try{
        await axios.post("http://localhost:5000/api/user/login", entr)
        .then((response)=>{
            if(response.status===200){
                commit("setStateAll", response.data);
                // console.log(response.data);
                // return response.status;
            }
        })
    }
    catch(e){
        console.log(e);
    }
    }
  },
  namespaced: true,
  
};