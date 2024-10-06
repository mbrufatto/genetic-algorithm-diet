<script setup>
import { state } from './state.js';

const props = defineProps({
  target: {
    type: Object,
  }
});
</script>

<template>
  <div class="flex justify-between items-center">
    <div class="text-xs min-w-32">
      Tipos selecionados:
    </div>
    <div class="flex flex-wrap">
      <div v-for="food in state.defaultFoodTypes" class="flex space-x-1 items-center p-2 text-xs">
        <input type="checkbox" v-model="target.typesSelected" :value="food.code" :checked="target.typesSelected.includes(food.code)"  >
        <label for="">{{ food.label }}</label>
      </div>
    </div>
  </div>
</template>
