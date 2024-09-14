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

    <div>
      <pre class="text-xs bg-gray-100 my-4 p-2">
TODO:
( ) Criar banco de dados com as informações da tabela TACO.
( ) Ao gerar dieta, enviar as variáveis do front para o back.
( ) Configurar as variáveis globais no front: TAMANHO_POPULACAO, MAXIMO_EVOLUCOES, ELITE_PROPORCAO, MUTACAO_PROPORCAO
( ) Criar novas refeições
( ) Perfil de dieta pré-definidas: 'Emagrecimento', 'Atleta', etc. Talvez até definir dietas por sexo/peso.
( ) Tornar layout responsivo.
      </pre>
    </div>
  </div>
</template>
