<script setup>
import { ref, watch } from 'vue';
import { defineEmits } from 'vue';

const props = defineProps({
    config: Object,
});

const emit = defineEmits(['update:config']);

const tamanhoPopulacao = ref(props.config?.tamanho_populacao || 1000);
const maximoEvolucoes = ref(props.config?.maximo_evolucoes || 150);
const eliteProporcao = ref(props.config?.elite_proporcao || 0.1);
const mutacaoProporcao = ref(props.config?.mutacao_proporcao || 0.05);

const updateConfig = () => {
    // Aqui você pode adicionar a lógica para enviar os dados atualizados para o backend
    console.log({
        tamanhoPopulacao: tamanhoPopulacao.value,
        maximoEvolucoes: maximoEvolucoes.value,
        eliteProporcao: eliteProporcao.value,
        mutacaoProporcao: mutacaoProporcao.value,
    });
};

// Watchers para detectar mudanças nos inputs e emitir o evento para o componente pai
watch([tamanhoPopulacao, maximoEvolucoes, eliteProporcao, mutacaoProporcao], () => {
  emit('update:config', {
    tamanho_populacao: tamanhoPopulacao.value,
    maximo_evolucoes: maximoEvolucoes.value,
    elite_proporcao: eliteProporcao.value,
    mutacao_proporcao: mutacaoProporcao.value,
  });
});
</script>

<template>
  <div class="flex items-center p-2 border rounded-lg border-gray-100 text-gray-800 bg-white">
    <h2 class="text-lg font-semibold mb-4 min-w-[255px]">Configurações</h2>

    <div class="flex space-x-2">

      <div class="flex flex-col">
        <label for="" class="block mb-1 text-xs font-medium text-gray-900">Tamanho População:</label>
        <input
          id="tamanhoPopulacao"
          type="number"
          v-model="tamanhoPopulacao"
          class="bg-white max-w-36 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400  block w-full p-2"
        />
      </div>

      <div class="flex flex-col">
        <label for="" class="block mb-1 text-xs font-medium text-gray-900">Máximo Evoluções:</label>
        <input
          id="maximoEvolucoes"
          type="number"
          v-model="maximoEvolucoes"
          class="bg-white max-w-36 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2"
        />
      </div>

      <div class="flex flex-col">
        <label for="" class="block mb-1 text-xs font-medium text-gray-900">Elite Proporção:</label>
        <input
          id="eliteProporcao"
          type="number"
          v-model="eliteProporcao"
          class="bg-white max-w-36 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2"
        />
      </div>

      <div class="flex flex-col">
        <label for="" class="block mb-1 text-xs font-medium text-gray-900">Mutação Proporção:</label>
        <input
          id="mutacaoProporcao"
          type="number"
          v-model="mutacaoProporcao"
          class="bg-white max-w-36 border border-gray-200 text-gray-900 text-sm rounded-lg caret-yellow-500 accent-yellow-400 focus:ring-yellow-500 focus:border-yellow-500 block w-full p-2"
        />
      </div>

    </div>

  </div>
</template>
