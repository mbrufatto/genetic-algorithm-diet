import random

from ..models.diet_command import DietaCommand
from ..queries.food_queries import get_food_by_category_list
from sqlalchemy.orm import Session

# Parâmetros configuráveis
TAMANHO_POPULACAO = 1000
MAXIMO_EVOLUCOES = 150
ELITE_PROPORCAO = 0.1
MUTACAO_PROPORCAO = 0.05

ALVO_CALORIAS = 1000
ALVO_PROTEINAS = 100
ALVO_LIPIDIOS = 200
ALVO_FIBRAS = 40
ALVO_CARBOIDRATOS = 100
MAX_PORCOES = 8


# Função para gerar um indivíduo aleatório
def gerar_individuo(alimentos):
    # TODO: fazer o algoritmo não selecionar as categorias e alimentos indesejados
    return random.sample(alimentos, MAX_PORCOES)


# Função de fitness (quanto mais próximo do alvo, melhor)
def calcular_fitness(individuo):
    (total_calorias,
     total_proteinas,
     total_lipidios,
     total_fibras,
     total_carboidratos) = calcular_macro_nutrientes(individuo)

    fitness = (
        abs(ALVO_CALORIAS - total_calorias)
        + abs(ALVO_PROTEINAS - total_proteinas)
        + abs(ALVO_LIPIDIOS - total_lipidios)
        + abs(ALVO_FIBRAS - total_fibras)
        + abs(ALVO_CARBOIDRATOS - total_carboidratos)
    )

    return fitness

def calcular_macro_nutrientes(individuo):
    total_calorias = sum([alimento["energy_kcal"] for alimento in individuo])
    total_proteinas = sum([alimento["protein_g"] for alimento in individuo])
    total_lipidios = sum([alimento["lipids_g"] for alimento in individuo])
    total_fibras = sum([alimento["dietary_fiber_g"] for alimento in individuo])
    total_carboidratos = sum([alimento["carbohydrate_g"] for alimento in individuo])

    return total_calorias, total_proteinas, total_lipidios, total_fibras, total_carboidratos

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


def generate_diet_on_command(db: Session, command: DietaCommand):
    global ALVO_CALORIAS, \
           MAX_PORCOES, \
           ALVO_FIBRAS, \
           ALVO_CARBOIDRATOS, \
           ALVO_LIPIDIOS, \
           ALVO_PROTEINAS

    ALVO_CALORIAS = command.calorias
    MAX_PORCOES = command.porcoes
    ALVO_FIBRAS = command.fibras
    ALVO_CARBOIDRATOS = command.carboidratos
    ALVO_LIPIDIOS = command.lipidios
    ALVO_PROTEINAS = command.proteinas

    return generate_diet(db, command.categorias)


def generate_diet(db: Session, categories=None):
    alimentos = [alimento.to_dict() for alimento in get_food_by_category_list(db, categories)]

    populacao = [gerar_individuo(alimentos) for _ in range(TAMANHO_POPULACAO)]

    executando = True
    geracao = 0

    while executando and geracao < MAXIMO_EVOLUCOES:

        populacao = evoluir_populacao(populacao, alimentos)

        geracao += 1

    # TODO: juntar os mesmos alimentos num único registro e somar seus nutrientes

    show_nutrients(populacao[0])
    return populacao[0]


def show_nutrients(individuo):
    (total_calorias,
     total_proteinas,
     total_lipidios,
     total_fibras,
     total_carboidratos) = calcular_macro_nutrientes(individuo)

    print("\n")
    print("\t\tDieta \t | \t Alvo")
    print("Calorias: \t", round(total_calorias, 1), "\t | \t ", ALVO_CALORIAS)
    print("Proteinas: \t", round(total_proteinas, 1), "\t | \t ", ALVO_PROTEINAS)
    print("Lipidios: \t", round(total_lipidios, 1), "\t | \t ", ALVO_LIPIDIOS)
    print("Colesterol: \t", round(total_fibras, 1), "\t | \t ", ALVO_FIBRAS)
    print(
        "Fibras: \t", round(total_carboidratos, 1), "\t | \t ", ALVO_CARBOIDRATOS
    )
