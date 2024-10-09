<script setup>
import Meal from './Meal.vue'
import Configs from './Configs.vue'
import { onBeforeMount } from 'vue';
import { state } from './state.js';
import { reactive } from 'vue';

const props = defineProps({
});

onBeforeMount(() => {
    state.meals = state.defaultMeals;
    state.config = state.default_config_parameter;
});

const updateConfig = (newConfig) => {
  Object.assign(state.config, newConfig);
};

</script>

<template>
  <div class="flex flex-col">

    <h1 class="font-semibold text-xl text-emerald-700 p-4">Dieta AG</h1>

    <div class="flex flex-col space-y-2 px-2 my-2">
      <Configs :config="config" @update:config="updateConfig" />
    </div>

    <div class="flex flex-col space-y-2 px-2">
      <Meal v-for="(meal) in state.meals" :config="meal" :paramsConfig="state.config" />
    </div>

  </div>
</template>
