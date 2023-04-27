<template>
    <div>
        <div>{{ mentor.name }}</div>
        <div>{{ mentor.salary }}</div>
    </div>
</template>

<script>
import useMentorStore from "@/stores/mentors.js";

export default {
    name: "MentorView",

    data() {
        return { 
            mentor: {},
        }
    },

    methods: { },

    props: {
        id: {
            type: String,
            required: true
        }
    },

    async created() {
        console.log("Открыт ментор с id = ", this.id);
        const store = useMentorStore();

        const mentor = await store.reqMentorsById(this.id);

        console.log(mentor);
        this.mentor =  mentor;

    }
}
</script>