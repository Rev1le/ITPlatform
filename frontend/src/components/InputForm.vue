<template>

    <div class="input_form" v-for="(input, index) in input_fields">
        <input 
            class="input-form"  
            :id="index"
            :type="input.type" 
            :placeholder="input.placeholder"
            :value="input.value"
            @input="sumbit"
        >
    </div>

</template>

<script lang="js">
export default {
    props: ["input_fields"],
    emits: ['update:input_fields'],
    methods: {
        sumbit(event) {
            this.input_fields[event.target.id].value = event.target.value;
            this.$emit('update:input_fields', this.input_fields);
        }
    }
}
</script>

<style>
input {
    margin: 5px 0;
    }
</style>