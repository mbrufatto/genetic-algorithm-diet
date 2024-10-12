import random

from ..models.diet_command import DietaCommand
from ..models.diet_config import DietaConfig
from ..queries.food_queries import get_food_by_category_list
from sqlalchemy.orm import Session

# Parâmetros configuráveis
TAMANHO_POPULACAO: int = 3000
MAXIMO_EVOLUCOES: int = 150
ELITE_PROPORCAO: float = 0.1
MUTACAO_PROPORCAO: float = 0.05

FITNESS_OBJETIVO = 30

ALVO_CALORIAS = 2000
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
    calcular_fitness(populacao_ordenada[0])

    elite_size = int(TAMANHO_POPULACAO * ELITE_PROPORCAO)
    return populacao_ordenada[:elite_size]

def crossover_um_ponto(pai, mae):
    ponto_corte = random.randint(1, len(pai) - 1)
    filho = pai[:ponto_corte] + mae[ponto_corte:]
    return filho

def mutacao_insercao(individuo, alimentos):
    idx1 = random.sample(range(len(individuo)), 1)
    idx2 = random.sample(range(len(alimentos)), 1)
    individuo.pop(idx1[0])
    individuo.insert(idx1[0], alimentos[idx2[0]])
    return individuo

def evoluir_populacao(populacao, alimentos):
    elites = selecionar_elite(populacao)
    nova_populacao = []
    while len(nova_populacao) < len(populacao) - len(elites):

        # Seleciona dois pais aleatórios da elite
        pai, mae = random.choices(elites, k=2)

        # Cruzamento
        filho = crossover_um_ponto(pai, mae)

        # Mutação
        if random.random() < MUTACAO_PROPORCAO:
            filho = mutacao_insercao(filho, alimentos)

        # Adiciona filho na população
        nova_populacao.append(filho)

    # Retorna a população evoluida
    return elites + nova_populacao


def generate_diet_on_command(db: Session, config: DietaConfig, command: DietaCommand):
    global ALVO_CALORIAS, \
           MAX_PORCOES, \
           ALVO_FIBRAS, \
           ALVO_CARBOIDRATOS, \
           ALVO_LIPIDIOS, \
           ALVO_PROTEINAS, \
           TAMANHO_POPULACAO, \
           MAXIMO_EVOLUCOES, \
           ELITE_PROPORCAO, \
           MUTACAO_PROPORCAO

    ALVO_CALORIAS = command.calorias
    MAX_PORCOES = command.porcoes
    ALVO_FIBRAS = command.fibras
    ALVO_CARBOIDRATOS = command.carboidratos
    ALVO_LIPIDIOS = command.lipidios
    ALVO_PROTEINAS = command.proteinas

    TAMANHO_POPULACAO = config.tamanho_populacao
    MAXIMO_EVOLUCOES = config.maximo_evolucoes
    ELITE_PROPORCAO = config.elite_proporcao
    MUTACAO_PROPORCAO = config.mutacao_proporcao

    return generate_diet(db, command.categorias)


def generate_diet(db: Session, categories=None):
    alimentos = [alimento.to_dict() for alimento in get_food_by_category_list(db, categories)]

    populacao = [gerar_individuo(alimentos) for _ in range(TAMANHO_POPULACAO)]

    executando = True
    geracao = 0

    while executando and geracao < MAXIMO_EVOLUCOES:
        populacao = evoluir_populacao(populacao, alimentos)
        melhor_fitness = calcular_fitness(populacao[0])

        if melhor_fitness <= FITNESS_OBJETIVO:
            break

        geracao += 1

    # TODO: juntar os mesmos alimentos num único registro e somar seus nutrientes

    print(f"Fitness objetivo alcançado na geração {geracao}")

    show_nutrients(populacao[0])
    return populacao[0]


def show_nutrients(individuo):
    (total_calorias,
     total_proteinas,
     total_lipidios,
     total_fibras,
     total_carboidratos) = calcular_macro_nutrientes(individuo)

    print("\n\n Configuração:\n ")
    print("Tamanho da população: \t", TAMANHO_POPULACAO)
    print("Máximo de evoluções: \t", MAXIMO_EVOLUCOES)
    print("Elite proporção: \t", ELITE_PROPORCAO)
    print("Mutação proporção: \t", MUTACAO_PROPORCAO)

    print("\n Detalhes da Dieta:\n ")

    print("\t\tDieta \t | \t Alvo")
    print("Calorias: \t", round(total_calorias, 1), "\t | \t ", ALVO_CALORIAS)
    print("Proteinas: \t", round(total_proteinas, 1), "\t | \t ", ALVO_PROTEINAS)
    print("Lipidios: \t", round(total_lipidios, 1), "\t | \t ", ALVO_LIPIDIOS)
    print("Fibras: \t", round(total_fibras, 1), "\t | \t ", ALVO_FIBRAS)
    print(
        "Carboidratos: \t", round(total_carboidratos, 1), "\t | \t ", ALVO_CARBOIDRATOS
    )
