<template>
	<p>Hi </p>
</template>

<script>
export default {
    props:{
        holder:{type: String,
        default:''},
        value : [String, Number],
    },
    methods:{
        updateInput(event){
            this.$emit("update:value", event.target.value)
        }
    }
}
</script>
