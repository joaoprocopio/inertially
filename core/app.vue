<template>
    <div>
        <h1>{{ props.title }}</h1>
        <h2>hello world!</h2>
    </div>
</template>

<script lang="js">
export default {
    props: {
        title: {
            type: String,
            required: true,
        }
    }
}
</script>
