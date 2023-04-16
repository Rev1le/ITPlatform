import axios from "axios";
export const vacantionStore = {
  state: () => ({
    vacantions: [
      ],
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
    getVacantions(state) {
      return state.vacantions;
    },
    // sortedVacantions(state) {
    //     return [...state.Vacantions].sort((vac1, vac2) => vac1[state.selectedSort]?.localeCompare(vac2[state.selectedSort]))
    // },
    sortedAndSearchedVacantions(state) {
        return [...state.vacantions].filter(Vacantions => Vacantions.name.toLowerCase().includes(state.searchQuery.toLowerCase()))
    }
    // getName(state) {
    //   return state.name;
    // },
    // getUser(state) {
    //   return state.user;
    // },
  },
  mutations: {
    setVacantions(state, vacantions) {
      state.vacantions = vacantions;
    },
    setSearchQuery(state, searchQuery) {

      state.searchQuery = searchQuery;
    },
    // setName(state, name) {
    //   state.name = name;
    // },
    // setUser(state, user) {
    //   state.user = user;
    // },

    // setStateAll(state, userData) {
    //   state.role = userData.role;
    //   state.name = userData.name;
    //   state.user = userData.user;
    // },
  },
  actions: {
    async reqVacantions({ commit }, entr) {
      try {
        await axios
          .post("http://localhost:5000/api/user/login", entr)
          .then((response) => {
            if (response.status === 200) {
              commit("setVacantions", response.data);
              // console.log(response.data);
              // return response.status;
            }
          });
      } catch (e) {
        console.log(e);
      }
    },
    async loadMoreVacantions({state, commit}) {
        try {
            commit('setPage', state.page + 1)
            const response = await axios.get('', {
                params: {
                    _page: state.page,
                    _limit: state.limit
                }
            });
            commit('setTotalPages', Math.ceil(response.headers['x-total-count'] / state.limit))
            commit('setPosts', [...state.posts, ...response.data]);
        } catch (e) {
            console.log(e)
        }
    },
    async reqVacantionById(id) {
      try {
        await axios
            .get(`localhost:8000/api/vacancy/${id}`)
            .then((response) => {
              if (response.status === 200) {
                return response.data;
              }
            });
      } catch (e) {
        console.log(e);
      }
    },
  },

  namespaced: true,
};
