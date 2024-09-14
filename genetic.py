import random

# TODO: Atualizar esse banco de dados com registros da tabela TACO
import db

# Parâmetros configuráveis
TAMANHO_POPULACAO = 1000
MAXIMO_EVOLUCOES = 150
ELITE_PROPORCAO = 0.1
MUTACAO_PROPORCAO = 0.05

ALVO_CALORIAS = 1500
ALVO_PROTEINAS = 60
ALVO_LIPIDIOS = 30
ALVO_COLESTEROL = 40
ALVO_CARBOIDRATOS = 50
MAX_PORCOES = 8


# Função para gerar um indivíduo aleatório
def gerar_individuo():
    # TODO: fazer o algoritmo não selecionar as categorias e alimentos indesejados
    return random.sample(db.alimentos, MAX_PORCOES)


# Função de fitness (quanto mais próximo do alvo, melhor)
def calcular_fitness(individuo):
    # TODO: trocar o 'colesterol' por fibras
    total_calorias = sum([alimento["calorias"] for alimento in individuo])
    total_proteinas = sum([alimento["proteinas"] for alimento in individuo])
    total_lipidios = sum([alimento["lipidios"] for alimento in individuo])
    total_colesterol = sum([alimento["colesterol"] for alimento in individuo])
    total_carboidratos = sum([alimento["carboidratos"] for alimento in individuo])

    fitness = (
        abs(ALVO_CALORIAS - total_calorias)
        + abs(ALVO_PROTEINAS - total_proteinas)
        + abs(ALVO_LIPIDIOS - total_lipidios)
        + abs(ALVO_COLESTEROL - total_colesterol)
        + abs(ALVO_CARBOIDRATOS - total_carboidratos)
    )

    return fitness


# Função para seleção dos melhores indivíduos (elite)
def selecionar_elite(populacao):
    populacao_ordenada = sorted(populacao, key=lambda x: calcular_fitness(x))

    # Melhor fitness
    print(str(round(calcular_fitness(populacao_ordenada[0]), 1)), end=", ")

    elite_size = int(TAMANHO_POPULACAO * ELITE_PROPORCAO)
    return populacao_ordenada[:elite_size]


def evoluir_populacao(populacao):

    elites = selecionar_elite(populacao)

    nova_populacao = []
    while len(nova_populacao) < len(populacao) - len(elites):
        # Seleciona dois pais aleatórios da elite
        pai, mae = random.choices(elites, k=2)

        filho = [None] * MAX_PORCOES

        for i in range(len(pai)):
            if random.random() < 0.5:
                filho[i] = pai[i]
            else:
                filho[i] = mae[i]

            # Mutação gerando um filho aleatório
            if random.random() < MUTACAO_PROPORCAO:
                filho[i] = random.choice(db.alimentos)

        # Adiciona filho na população
        nova_populacao.append(filho)

    # Retorna a população evoluida
    return elites + nova_populacao


def generate_diet():
    populacao = [gerar_individuo() for _ in range(TAMANHO_POPULACAO)]

    executando = True
    geracao = 0

    while executando and geracao < MAXIMO_EVOLUCOES:

        populacao = evoluir_populacao(populacao)

        geracao += 1

    # TODO: juntar os mesmos alimentos num único registro e somar seus nutrientes

    return populacao[0]
