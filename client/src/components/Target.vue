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

    <div class="flex flex-wrap space-x-2">
      <div>
        <label for="number-input" class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Número porções:</label>
        <input type="number" v-model="target.servings" class="bg-gray-50 max-w-32 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2">
      </div>

      <div>
        <label for="number-input" class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Calorias:</label>
        <input type="number" v-model="target.calories" class="bg-gray-50 max-w-32 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2">
      </div>

      <div>
        <label for="number-input" class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Proteínas:</label>
        <input type="number" v-model="target.proteins" class="bg-gray-50 max-w-32 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2">
      </div>

      <div>
        <label for="number-input" class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Lipídios:</label>
        <input type="number" v-model="target.lipids" class="bg-gray-50 max-w-32 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2">
      </div>

      <div>
        <label for="number-input" class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Carboidratos:</label>
        <input type="number" v-model="target.carbohydrates" class="bg-gray-50 max-w-32 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2">
      </div>

      <div>
        <label for="number-input" class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Fibras:</label>
        <input type="number" v-model="target.fibers" class="bg-gray-50 max-w-32 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2">
      </div>
    </div>

  </div>
</template>




