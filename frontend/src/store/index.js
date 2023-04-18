import { createStore } from 'vuex';
import { userStore } from "./userStore";
import { vacantionStore } from "./vacantionStore";
import { MentorsStore } from "./MentorsStore";

export default createStore(
    {
        state: { },
        getters: { },
        mutations: {},
        actions: {},
        modules: {
            userStore: userStore,
            vacantionStore: vacantionStore,
            MentorsStore: MentorsStore,
        }
    }
)
