import axios from "axios";
import {defineStore} from 'pinia';

const useVacantionStore = defineStore('vacantions', {
    
    state: () => ({
        vacantions: [],
        selectedSort: "",
        searchQuery: "",
        page: 1,
        limit: 3,
        totalPages: 0,
        sortOptions: [
            { value: "title", name: "По названию" },
            { value: "body", name: "По содержимому" },
        ],
    }),

    getters: {
        getVacantions(state) {return state.vacantions;},
        
        sortedAndSearchedVacantions(state) {
            return [...state.vacantions]
                .filter(Vacantions => Vacantions.name.toLowerCase()
                .includes(state.searchQuery.toLowerCase()))
        }
    },
    actions: {
      async reqVacantions(entr) {
          console.log(entr);
          try {

            let response = await axios.get("http://localhost:8000/api/vacancy/all", {});
            
            if (response.status === 200) {
              console.log('Полученные вакансии:\n', response.data);
              this.vacantions = response.data;
            }

          } 
          catch (e) {
            console.log(e);
          }
        },
        // async loadMoreVacantions({state, commit}) {
        //     try {
        //         commit('setPage', state.page + 1)
        //         const response = await axios.get('', {
        //             params: {
        //                 _page: state.page,
        //                 _limit: state.limit
        //             }
        //         });
        //         commit('setTotalPages', Math.ceil(response.headers['x-total-count'] / state.limit))
        //         commit('setPosts', [...state.posts, ...response.data]);
        //     } catch (e) {
        //         console.log(e)
        //     }
        // },
        async reqVacantionById(id){
          console.log('vhod1');
          
          let config = {
            headers: {
              "content-type": "application/json",
              "token": "MVIwoTovdTi6mM89opYoRMy5syGGeMTh5e1boOPSmXc",
            }
          }
          
          try {
            return await axios.get(`http://localhost:8000/api/vacancy/${id}`, config);
          } catch (e) {
            console.log("We have http error", e);
          }
        },
    },
});

export default useVacantionStore