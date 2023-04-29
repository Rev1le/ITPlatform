<template>

    <input  
        class="input-form"  
        :type="field.type" 
        :placeholder="field.placeholder"
        :value="field.value"
        @input="submit"
        
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
            this.$emit('update:field', {
                type: this.field.type,
                placeholder: this.field.placeholder,
                value: event.target.value,
            })
        }
    }
}

</script>

<style scoped>
.input {
    
}
</style>