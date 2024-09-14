<script setup>
import { state } from './state.js';

const props = defineProps({
  typesSelected: {
    type: Array,
    default: () => []
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
        <input type="checkbox" name="" id="" :checked="typesSelected.includes(food)">
        <label for="">{{ food }}</label>
      </div>
    </div>
  </div>
</template>
