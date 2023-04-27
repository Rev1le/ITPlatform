import { defineStore } from 'pinia';
import axios from "axios";

const useMentorStore = defineStore('mentors', {
    state: () => ({
        mentors: [],
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
        getMentors(state) {
          return state.mentors;
        },
        sortedAndSearchedMentors(state) {
            return [...state.mentors]
                .filter(Mentors => Mentors.name.toLowerCase()
                .includes(state.searchQuery.toLowerCase()))
        }
      },

      actions: {
        async reqMentors() {
          try {

            const response = await axios.get("http://localhost:8000/api/mentor/all", {});
            if (response.status === 200) {

                this.mentors = response.data;
                console.log(this.mentors);
            }

          } catch (e) {
            console.log(e);
          }
        },

        async reqMentorsById(id) {
          try {
            const response = await axios.get(`http://localhost:8000/api/mentor/${id}`);
            return response.data
          } catch (e) {
            console.log(e);
          }
        },
        // async loadMoreMentors({state, commit}) {
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
        // }
      },
});

export default useMentorStore
