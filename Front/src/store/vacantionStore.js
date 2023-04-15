import axios from "axios";
export const vacantionStore = {
  state: () => ({
    vacantions: [
      {
        name: "Rust разработчик",
        salary: "Зарплата договорная",
        desription:
          "Требуется Python-разработчик для работы в компании. Кандидат должен иметь опыт работы с языком программирования Python и знание основных библиотек и фреймворков. Основные обязанности включают разработку и поддержку программного обеспечения на Python, написание и отладку кода, тестирование и оптимизацию производительности.",
        skills: ["Биба", "боба", "python"],
      },
      {
        name: "React разработчик",
        salary: "Зарплата договорная",
        desription:
          "Требуется Python-разработчик для работы в компании. Кандидат должен иметь опыт работы с языком программирования Python и знание основных библиотек и фреймворков. Основные обязанности включают разработку и поддержку программного обеспечения на Python, написание и отладку кода, тестирование и оптимизацию производительности.",
        skills: ["Биба", "боба", "python"],
      },
      {
        name: "Nim разработчик",
        salary: "Зарплата договорная",
        desription:
          "Требуется Python-разработчик для работы в компании. Кандидат должен иметь опыт работы с языком программирования Python и знание основных библиотек и фреймворков. Основные обязанности включают разработку и поддержку программного обеспечения на Python, написание и отладку кода, тестирование и оптимизацию производительности.",
        skills: ["Биба", "боба", "python"],
      },
      {
        name: "JS разработчик",
        salary: "Зарплата договорная",
        desription:
          "Требуется Python-разработчик для работы в компании. Кандидат должен иметь опыт работы с языком программирования Python и знание основных библиотек и фреймворков. Основные обязанности включают разработку и поддержку программного обеспечения на Python, написание и отладку кода, тестирование и оптимизацию производительности.",
        skills: ["Биба", "боба", "python"],
      },
      {
        name: "Питон разработчик",
        salary: "Зарплата договорная",
        desription:
          "Требуется Python-разработчик для работы в компании. Кандидат должен иметь опыт работы с языком программирования Python и знание основных библиотек и фреймворков. Основные обязанности включают разработку и поддержку программного обеспечения на Python, написание и отладку кода, тестирование и оптимизацию производительности.",
        skills: ["Биба", "боба", "python"],
      },
      {
        name: "React разработчик",
        salary: "Зарплата договорная",
        desription:
          "Требуется Python-разработчик для работы в компании. Кандидат должен иметь опыт работы с языком программирования Python и знание основных библиотек и фреймворков. Основные обязанности включают разработку и поддержку программного обеспечения на Python, написание и отладку кода, тестирование и оптимизацию производительности.",
        skills: ["Биба", "боба", "python"],
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
              commit("setStateAll", response.data);
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
    }
  },
  namespaced: true,
};
