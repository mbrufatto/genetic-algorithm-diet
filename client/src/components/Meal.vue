<script setup>
import { ref, computed } from 'vue';
import FoodTypes from './FoodTypes.vue';
import Target from './Target.vue';
import axios from 'axios';

const props = defineProps({
    config: Object,
    paramsConfig: Object
});

let diet = ref(null);
let groupResults = ref(false);

function postGeneratedDiet() {
  let generateDietRequest = {
    "meta": {
      porcoes: props.config.target.servings,
      calorias: props.config.target.calories,
      proteinas: props.config.target.proteins,
      lipidios: props.config.target.lipids,
      carboidratos: props.config.target.carbohydrates,
      fibras: props.config.target.fibers,
      categorias: props.config.target.typesSelected
    },
    "config": props.paramsConfig
  }

  axios.post("http://127.0.0.1:5000/diet/create", generateDietRequest)
    .then((response) => {
      this.diet = response.data;
    })
    .catch((error) => {
      console.error("Erro ao obter a dieta:", error);
    });
}

function formatDecimal(value, digits) {
    return value.toLocaleString("pt-BR", {
        minimumFractionDigits: digits,
        maximumFractionDigits: digits,
    });
}

const groupedDiet = computed(() => {
  let grouped = [];

  if (diet.value) {
    diet.value.forEach(person => {
    let found = grouped.find(p => p.name === person.name);

    if (found) {
      found.count += 1;
      found.energy_kcal += found.energy_kcal;
      found.protein_g += found.protein_g;
      found.lipids_g += found.lipids_g;
      found.carbohydrate_g += found.carbohydrate_g;
      found.dietary_fiber_g += found.dietary_fiber_g;
    } else {
      grouped.push({...person, count: 1});
    }
  });
  }
  return grouped;
})

</script>

<template>
  <div class="flex flex-col md:flex-row items-center space-x-2 border rounded border-gray-300 text-gray-800">

    <!-- Título -->
    <div class="min-w-32 font-semibold w-full md:w-1/12 text-center">
        {{ config.title }}
    </div>

    <!-- Configurações -->
    <div class="flex flex-col space-y-2 w-full md:w-6/12 my-4">
        <FoodTypes :target="config.target"></FoodTypes>
        <Target :target="config.target"></Target>
    </div>

    <!-- Resultado -->
    <div class="w-full md:w-5/12">

      <!-- Tabela Resultado -->
      <div v-if="diet != null" class="flex flex-col relative overflow-x-auto items-center p-2">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 font-mono">
          <thead class="text-xs text-gray-700 bg-gray-50">
            <tr>
              <th class="text-center" v-if="groupResults">Quant.</th>
              <th class="text-center">Alimento</th>
              <th class="text-center">Categoria</th>
              <th class="text-right">Calorias (kcal)</th>
              <th class="text-right">Proteínas (g)</th>
              <th class="text-right">Lipidios (g)</th>
              <th class="text-right">Carboidratos (g)</th>
              <th class="text-right">Fibra (g)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="food in (groupResults ? groupedDiet : diet )" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 border-b">
              <td class="text-xs text-center" v-if="groupResults">{{ food.count }}</td>
              <td class="text-xs">{{ food.name }}</td>
              <td class="text-xs">{{ food.category }}</td>
              <td class="text-right">{{ formatDecimal(food.energy_kcal, 1) }}</td>
              <td class="text-right">{{ formatDecimal(food.protein_g, 1) }}</td>
              <td class="text-right">{{ formatDecimal(food.lipids_g, 1) }}</td>
              <td class="text-right">{{ formatDecimal(food.carbohydrate_g, 1) }}</td>
              <td class="text-right">{{ formatDecimal(food.dietary_fiber_g, 1) }}</td>
            </tr>
            <tr>
              <td v-if="groupResults"></td>
              <td colspan="2" class="text-right text-lg font-bold">
                  Total
              </td>
              <td class="text-right font-semibold">
                {{ formatDecimal(diet.reduce((acc, f) => {return acc + f.energy_kcal}, 0), 1) }}
               </td>
              <td class="text-right font-semibold">
                {{ formatDecimal(diet.reduce((acc, f) => {return acc + f.protein_g}, 0), 1) }}
              </td>
              <td class="text-right font-semibold">
                {{ formatDecimal(diet.reduce((acc, f) => {return acc + f.lipids_g}, 0), 1) }}
              </td>
              <td class="text-right font-semibold">
                {{ formatDecimal(diet.reduce((acc, f) => {return acc + f.carbohydrate_g}, 0), 1) }}
              </td>
              <td class="text-right font-semibold">
                {{ formatDecimal(diet.reduce((acc, f) => {return acc + f.dietary_fiber_g}, 0), 1) }}
              </td>
            </tr>
          </tbody>
        </table>

        <div class="flex justify-end text-xs space-x-2 w-full">
          <input type="checkbox" name="" id="" v-model="groupResults">
          <span>Agrupar resultados</span>
        </div>

        <!-- Refazer dieta -->
        <div class="p-4">
          <button @click="postGeneratedDiet()" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-2 py-1 me-1 mb-1 focus:outline-none">
            Refazer dieta
          </button>
        </div>
      </div>

      <!-- Gerar dieta -->
      <div v-else class="flex justify-center">
        <button @click="postGeneratedDiet()" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-2 py-1 me-1 mb-1 focus:outline-none">
          Gerar dieta
        </button>
      </div>
    </div>

  </div>
</template>
