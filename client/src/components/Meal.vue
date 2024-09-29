<script setup>
import { ref } from 'vue';
import FoodTypes from './FoodTypes.vue';
import Target from './Target.vue';
import axios from 'axios';

const props = defineProps({
    config: Object,
});

let diet = ref(null);

function getGeneratedDiet() {
  // TODO: enviar as propriedades como parâmetros
  axios.get('http://127.0.0.1:5000/get-diet')
    .then((response) => {
      this.diet = response.data;
      console.log(this.diet);
    })
}

</script>

<template>
  <div class="flex items-center p-2 border rounded border-gray-300 text-gray-800">
    <div class="min-w-32 font-semibold">
        {{ config.title }}
    </div>
    <div class="flex flex-col space-y-2">
        <FoodTypes :types-selected="config.typesSelected"></FoodTypes>
        <Target :target="config.target"></Target>
    </div>

    <div v-if="diet != null" class="flex flex-col relative overflow-x-auto w-1/3 min-w-[500px] items-center">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-xs text-gray-700 bg-gray-50">
          <tr>
            <th>Alimento</th>
            <th>Categoria</th>
            <th>Calorias (kcal)</th>
            <th>Proteínas (g)</th>
            <th>Lipidios (g)</th>
            <th>Carboidratos (g)</th>
            <th>Fibra (g)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="food in diet" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50  border-b">
            <td>{{ food.name }}</td>
            <td>{{ food.category }}</td>
            <td>{{ food.energy_kcal }}</td>
            <td>{{ food.protein_g }}</td>
            <td>{{ food.lipids_g }}</td>
            <td>{{ food.carbohydrate_g }}</td>
            <td>{{ food.dietary_fiber_g }}</td>
          </tr>
        </tbody>
      </table>
      <div class="p-1">
        <button @click="getGeneratedDiet()" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-2 py-1 me-1 mb-1 focus:outline-none">
          Refazer dieta
        </button>
      </div>
    </div>
    <div v-else class="flex justify-center w-1/3">
      <button @click="getGeneratedDiet()" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-2 py-1 me-1 mb-1 focus:outline-none">
        Gerar dieta
      </button>
    </div>

  </div>
</template>
