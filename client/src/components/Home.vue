<script setup>
import Meal from './Meal.vue'
import { onBeforeMount } from 'vue';
import { state } from './state.js';

const props = defineProps({
});

onBeforeMount(() => {
    state.meals = state.defaultMeals;
});

</script>

<template>
  <div class="flex flex-col">

    <h1 class="font-semibold text-xl text-emerald-700 p-4">Dieta AG</h1>

    <div class="flex flex-col space-y-2 px-2">
        <Meal v-for="(meal) in state.meals" :config="meal" />
    </div>

  </div>
</template>
