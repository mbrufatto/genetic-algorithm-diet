<script setup>
import Meal from './Meal.vue'
import Configs from './Configs.vue'
import { onBeforeMount } from 'vue';
import { state } from './state.js';

onBeforeMount(() => {
    state.meals = state.defaultMeals;
    state.config = state.default_config_parameter;
});

const updateConfig = (newConfig) => {
  Object.assign(state.config, newConfig);
};

</script>

<template>
  <div class="flex flex-col bg-gray-50 min-h-full space-y-8 h-full">

    <div class="p-4">
        <svg height="25px" version="1.1" viewBox="0 0 172.07 38.114" xmlns="http://www.w3.org/2000/svg">
        <g transform="translate(-41.931 -84.212)" stroke-width=".26458">
          <text x="38.490334" y="121.7901" fill="#73d216" font-family="Garuda" font-size="44.686px" style="line-height:1.25" xml:space="preserve"><tspan x="38.490334" y="121.7901" fill="#73d216" font-family="Garuda" stroke-width=".26458">Dieta</tspan></text>
          <text x="145.50024" y="121.61276" fill="#c4a000" font-family="sans-serif" font-size="50.392px" style="line-height:1.25" xml:space="preserve"><tspan x="145.50024" y="121.61276" fill="#c4a000" stroke-width=".26458">AG</tspan></text>
        </g>
      </svg>
    </div>

    <div class="flex flex-col px-1 lg:px-4 shadow-sm">
      <Configs :config="state.config" @update:config="updateConfig" />
    </div>

    <div class="flex flex-col space-y-8 px-1 lg:px-4">
      <Meal v-for="(meal) in state.meals" :config="meal" :paramsConfig="state.config" />
    </div>

  </div>
</template>
