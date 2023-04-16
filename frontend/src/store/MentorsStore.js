import axios from "axios";
export const MentorsStore = {
  state: () => ({
    Mentors: [
      {
        name: "Мария Иванова",
        salary: "Опытный ментор",
        vocation:"Pthon & SQL",
        desription:
          "Хочу помочь начинающим",
        skills: ["sql", "Soft", "python"],
      },
      {
        name: "Иван Козюков",
        salary: "Опытный ментор",
        vocation:"Pthon & SQL",
        desription:
         "Хочу помочь начинающим разработчикам",
        skills: ["sql", "Soft", "python"],
      },
      {
        name: "Король и Шут",
        salary: "Опытный ментор",
        vocation:"Pthon & SQL",
        desription:
          "Помогу в сборе молниц",
        skills: ["Молнии","Дурак"],
      },
      {
        name: "Герванд из рыбии",
        salary: "Опытный ментор",
        vocation:"Чудища и люди",
        desription:
          "Помогу с карточной игрой ХВЫНД",
        skills: ["Меч", "Единоборства", "Nim"],
      },
      {
        name: "Андреас Румпф",
        salary: "Опытный ментор",
        vocation:"Nim",
        desription:
          "Покажите мне код и я скажу вам подумать дважды",
        skills: ["Won`t fix", "Nim"],
      },
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
    getMentors(state) {
      return state.Mentors;
    },
    // sortedVacantions(state) {
    //     return [...state.Vacantions].sort((vac1, vac2) => vac1[state.selectedSort]?.localeCompare(vac2[state.selectedSort]))
    // },
    sortedAndSearchedMentors(state) {
        return [...state.Mentors].filter(Mentors => Mentors.name.toLowerCase().includes(state.searchQuery.toLowerCase()) )
    }
    // getName(state) {
    //   return state.name;
    // },
    // getUser(state) {
    //   return state.user;
    // },
  },
  mutations: {
    setMentors(state, Mentors) {
      state.Mentors = Mentors;
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
    async reqMentors({ commit }) {
      try {
        await axios
          .get("http://localhost:5000/api/user/login",)
          .then((response) => {
            if (response.status === 200) {
              commit("setMentors", response.data);
              // console.log(response.data);
              // return response.status;
            }
          });
      } catch (e) {
        console.log(e);
      }
    },
    async reqMentorsById(id) {
      try {
        await axios
          .get(`тут_типо_путь/${id}`)
          .then((response) => {
            if (response.status === 200) {
              return response.data;
            }
          });
      } catch (e) {
        console.log(e);
      }
    },
    async loadMoreMentors({state, commit}) {
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
    }
  },
  namespaced: true,
};
