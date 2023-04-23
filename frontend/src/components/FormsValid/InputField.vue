<template>

    <input  
        class="input"  
        :type="field.type" 
        :placeholder="field.placeholder"
        :value="field.value"
        @input="sumbit"
    />

</template>

<script lang="js">
// Данный компонент является альтернативой InputForm

export default {
    props: {
        field: {
            type: Object,
            required: true
        }
    },
    emits: ['update:field'],
    methods: {
        async submit(event) {
            console.log(event);
           // this.$emit('submit', )
        }
    }
}

</script>

<style scoped>
.input {
    
}
</style>