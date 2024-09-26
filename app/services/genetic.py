import random
from ..queries.food_queries import get_all_food, get_foods_by_category
from sqlalchemy.orm import Session

# Parâmetros configuráveis
TAMANHO_POPULACAO = 1000
MAXIMO_EVOLUCOES = 150
ELITE_PROPORCAO = 0.1
MUTACAO_PROPORCAO = 0.05

ALVO_CALORIAS = 1500
ALVO_PROTEINAS = 60
ALVO_LIPIDIOS = 30
ALVO_FIBRAS = 40
ALVO_CARBOIDRATOS = 50
MAX_PORCOES = 8

# Função para gerar um indivíduo aleatório
def gerar_individuo(alimentos):
    # TODO: fazer o algoritmo não selecionar as categorias e alimentos indesejados
    return random.sample(alimentos, MAX_PORCOES)

# Função de fitness (quanto mais próximo do alvo, melhor)
def calcular_fitness(individuo):
    # TODO: trocar o 'colesterol' por fibras
    total_calorias = sum([alimento["energy_kcal"] for alimento in individuo])
    total_proteinas = sum([alimento["protein_g"] for alimento in individuo])
    total_lipidios = sum([alimento["lipids_g"] for alimento in individuo])
    total_fibras = sum([alimento["dietary_fiber_g"] for alimento in individuo])
    total_carboidratos = sum([alimento["carbohydrate_g"] for alimento in individuo])

    fitness = (
        abs(ALVO_CALORIAS - total_calorias)
        + abs(ALVO_PROTEINAS - total_proteinas)
        + abs(ALVO_LIPIDIOS - total_lipidios)
        + abs(ALVO_FIBRAS - total_fibras)
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


def evoluir_populacao(populacao, alimentos):

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
                filho[i] = random.choice(alimentos)

        # Adiciona filho na população
        nova_populacao.append(filho)

    # Retorna a população evoluida
    return elites + nova_populacao


def generate_diet(db: Session):
    # Consulta todos os alimentos do banco de dados
    alimentos = [alimento.to_dict() for alimento in get_all_food(db)]

    populacao = [gerar_individuo(alimentos) for _ in range(TAMANHO_POPULACAO)]

    executando = True
    geracao = 0

    while executando and geracao < MAXIMO_EVOLUCOES:

        populacao = evoluir_populacao(populacao, alimentos)

        geracao += 1

    # TODO: juntar os mesmos alimentos num único registro e somar seus nutrientes

    return populacao[0]
