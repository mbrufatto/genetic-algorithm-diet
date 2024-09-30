<script setup>
import { ref, watch } from 'vue';
import { defineEmits } from 'vue';
import axios from 'axios';

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
  <div class="flex items-center p-2 border rounded border-gray-300 text-gray-800">
    <h2 class="text-lg font-semibold mb-4 min-w-[255px]">Configurações</h2>

    <div class="flex flex-col space-y-2">
    </div>

    <div class="flex flex-col space-y-2">
    </div>

    <div class="flex flex-col relative overflow-x-auto w-1/3 min-w-[750px] items-center">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-xs text-gray-700 bg-gray-50">
          <tr>
            <th>Tamanho População</th>
            <th>Máximo Evoluções</th>
            <th>Elite Proporção</th>
            <th>Mutação Proporção</th>
          </tr>
        </thead>
        <tbody>
          <tr v-bind:class="config" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50  border-b">
            <td><input
          id="tamanhoPopulacao"
          type="number"
          v-model="tamanhoPopulacao"
          class="border border-gray-300 rounded p-2"
        /></td>
            <td><input
          id="maximoEvolucoes"
          type="number"
          v-model="maximoEvolucoes"
          class="border border-gray-300 rounded p-2"
        /></td>
            <td><input
          id="eliteProporcao"
          type="number"
          step="0.01"
          v-model="eliteProporcao"
          class="border border-gray-300 rounded p-2"
        /></td>
            <td><input
          id="mutacaoProporcao"
          type="number"
          step="0.01"
          v-model="mutacaoProporcao"
          class="border border-gray-300 rounded p-2"
        /></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>