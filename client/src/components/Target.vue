<script setup>

const props = defineProps({
  target: {
    type: Object,
    required: true,
  }
});

</script>

<template>
  <div class="flex items-center">
    <div class="text-xs min-w-32">
      Valores alvo:
    </div>

    <div class="flex flex-wrap">
      <div class="mx-1">
        <label for="number-input" class="block mb-1 text-xs font-medium text-gray-900">Número porções:</label>
        <input type="number" v-model="target.servings" class="bg-white max-w-24 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2">
      </div>

      <div class="mx-1">
        <label for="number-input" class="block mb-1 text-xs font-medium text-gray-900">Calorias:</label>
        <input type="number" v-model="target.calories" class="bg-white max-w-24 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2">
      </div>

      <div class="mx-1">
        <label for="number-input" class="block mb-1 text-xs font-medium text-gray-900">Proteínas:</label>
        <input type="number" v-model="target.proteins" class="bg-white max-w-24 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2">
      </div>

      <div class="mx-1">
        <label for="number-input" class="block mb-1 text-xs font-medium text-gray-900">Lipídios:</label>
        <input type="number" v-model="target.lipids" class="bg-white max-w-24 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2">
      </div>

      <div class="mx-1">
        <label for="number-input" class="block mb-1 text-xs font-medium text-gray-900">Carboidratos:</label>
        <input type="number" v-model="target.carbohydrates" class="bg-white max-w-24 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2">
      </div>

      <div class="mx-1">
        <label for="number-input" class="block mb-1 text-xs font-medium text-gray-900">Fibras:</label>
        <input type="number" v-model="target.fibers" class="bg-white max-w-24 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2">
      </div>
    </div>

  </div>
</template>




