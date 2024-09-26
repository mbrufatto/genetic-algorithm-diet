import os
import time
import random
import pygame
import sys

import db  # Certifique-se de que o módulo db está acessível

# Parâmetros configuráveis
TAMANHO_POPULACAO = int(os.getenv('TAMANHO_POPULACAO', 1000))
MAXIMO_EVOLUCOES = int(os.getenv('MAXIMO_EVOLUCOES', 150))
ELITE_PROPORCAO = float(os.getenv('ELITE_PROPORCAO', 0.1))
MUTACAO_PROPORCAO = float(os.getenv('MUTACAO_PROPORCAO', 0.05))

ALVO_CALORIAS = int(os.getenv('ALVO_CALORIAS', 1500))
ALVO_PROTEINAS = int(os.getenv('ALVO_PROTEINAS', 60))
ALVO_LIPIDIOS = int(os.getenv('ALVO_LIPIDIOS', 30))
ALVO_COLESTEROL = int(os.getenv('ALVO_COLESTEROL', 40))
ALVO_CARBOIDRATOS = int(os.getenv('ALVO_CARBOIDRATOS', 50))
MAX_PORCOES = int(os.getenv('MAX_PORCOES', 8))
TEMPO_ESPERA = float(os.getenv('TEMPO_ESPERA', 1))
PLOTAR_GRAFICO = bool(os.getenv('PLOTAR_GRAFICO', True))

MELHOR_INDIVIDUO = None
DADOS_EVOLUCAO = []

# Inicializando o Pygame
pygame.init()
LARGURA_TELA = 1000  # Aumentando a largura
ALTURA_TELA = 800  # Aumentando a altura
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Evolução de Nutrientes")


# Função para gerar um indivíduo aleatório
def gerar_individuo():
    return random.sample(db.alimentos, MAX_PORCOES)


# Função de fitness (quanto mais próximo do alvo, melhor)
def calcular_fitness(individuo):
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
    global MELHOR_INDIVIDUO
    MELHOR_INDIVIDUO = populacao_ordenada[0]
    fitness = round(calcular_fitness(MELHOR_INDIVIDUO), 1)

    print(str(fitness), end=", ")
    elite_size = int(TAMANHO_POPULACAO * ELITE_PROPORCAO)
    return populacao_ordenada[:elite_size]


def evoluir_populacao(populacao):
    time.sleep(TEMPO_ESPERA)
    elites = selecionar_elite(populacao)
    nova_populacao = []
    while len(nova_populacao) < len(populacao) - len(elites):
        pai, mae = random.choices(elites, k=2)

        filho = [None] * MAX_PORCOES
        for i in range(len(pai)):
            if random.random() < 0.5:
                filho[i] = pai[i]
            else:
                filho[i] = mae[i]

            if random.random() < MUTACAO_PROPORCAO:
                filho[i] = random.choice(db.alimentos)

        nova_populacao.append(filho)
    return elites + nova_populacao


def calcular_totais(individuo, campo):
    return sum([alimento[campo] for alimento in individuo])

def desenhar_legendas():
    font = pygame.font.Font(None, 24)
    legendas = ["Fitness"]
    cores = [
        (255, 0, 0),  # Fitness
    ]

    for i, (legenda, cor) in enumerate(zip(legendas, cores)):
        label = font.render(legenda, True, cor)
        tela.blit(label, (LARGURA_TELA - 150, 50 + i * 20))  # Melhor posicionamento

def desenhar_eixos():
    pygame.draw.line(tela, (0, 0, 0), (50, ALTURA_TELA - 50), (LARGURA_TELA - 50, ALTURA_TELA - 50), 2)  # Eixo X
    pygame.draw.line(tela, (0, 0, 0), (50, ALTURA_TELA - 50), (50, 50), 2)  # Eixo Y

    # Rótulos do eixo X
    font = pygame.font.Font(None, 24)
    for i in range(0, MAXIMO_EVOLUCOES + 1, 10):
        if i < MAXIMO_EVOLUCOES:
            x = 50 + (i * (LARGURA_TELA - 100) // MAXIMO_EVOLUCOES)
            y = ALTURA_TELA - 30
            label = font.render(str(i), True, (0, 0, 0))
            tela.blit(label, (x, y))

    # Rótulos do eixo Y (0 a 200 de 20 em 20)
    for i in range(0, 201, 20):
        y = ALTURA_TELA - 50 - (i * (ALTURA_TELA - 100) // 200)
        if y > 50:
            label = font.render(str(i), True, (0, 0, 0))
            tela.blit(label, (20, y))

def desenhar_nutriente_continuo(tela, cor, dados):
    for i in range(len(dados) - 1):
        valor_atual = dados[i]
        valor_proximo = dados[i + 1]
        scaled_current = (valor_atual / 200) * (ALTURA_TELA - 100)
        scaled_next = (valor_proximo / 200) * (ALTURA_TELA - 100)

        pygame.draw.line(
            tela,
            cor,
            (50 + i * (LARGURA_TELA - 100) // MAXIMO_EVOLUCOES, ALTURA_TELA - 50 - scaled_current),
            (50 + (i + 1) * (LARGURA_TELA - 100) // MAXIMO_EVOLUCOES, ALTURA_TELA - 50 - scaled_next),
            2
        )


def plotar_dados(tela, dados, geracao):
    fitness_dados = [valor[1] for valor in dados]  # Fitness para plotar
    # proteinas_dados = [valor[2] for valor in dados]  # Proteínas
    # lipidios_dados = [valor[3] for valor in dados]  # Lipídios
    # colesterol_dados = [valor[4] for valor in dados]  # Colesterol
    # carboidratos_dados = [valor[5] for valor in dados]  # Carboidratos

    # Cores
    cores = [
        (255, 0, 0)        # Fitness
        # (0, 255, 0),        # Proteínas
        # (0, 0, 255),        # Lipídios
        # (255, 255, 0),      # Colesterol
        # (128, 0, 128)       # Carboidratos
    ]

    # Plotar o fitness contínuo
    desenhar_nutriente_continuo(tela, cores[0], fitness_dados)

    # Plotar os outros nutrientes como pontos
    # for i in range(geracao):
    #     if i < len(dados):
    #         valor = dados[i]
    #         # Plota os nutrientes
    #         # desenhar_nutriente(tela, cores[1], i, valor[2])  # Proteínas
    #         # desenhar_nutriente(tela, cores[2], i, valor[3])  # Lipídios
    #         # desenhar_nutriente(tela, cores[3], i, valor[4])  # Colesterol
    #         # desenhar_nutriente(tela, cores[4], i, valor[5])  # Carboidratos

def iniciar():
    populacao = [gerar_individuo() for _ in range(TAMANHO_POPULACAO)]
    clock = pygame.time.Clock()

    executando = True
    geracao = 0
    global MELHOR_INDIVIDUO

    while executando and geracao < MAXIMO_EVOLUCOES:
        populacao = evoluir_populacao(populacao)

        total_proteinas = calcular_totais(MELHOR_INDIVIDUO, "proteinas")
        total_lipidios = calcular_totais(MELHOR_INDIVIDUO, "lipidios")
        total_colesterol = calcular_totais(MELHOR_INDIVIDUO, "colesterol")
        total_carboidratos = calcular_totais(MELHOR_INDIVIDUO, "carboidratos")

        fitness = calcular_fitness(MELHOR_INDIVIDUO)
        DADOS_EVOLUCAO.append((geracao, fitness, total_proteinas, total_lipidios, total_colesterol, total_carboidratos))
        geracao += 1

        # Visualização no Pygame
        tela.fill((255, 255, 255))  # Limpa a tela
        desenhar_eixos()  # Desenha os eixos
        plotar_dados(tela, DADOS_EVOLUCAO, geracao)  # Plota os dados
        desenhar_legendas()  # Desenha as legendas

        pygame.display.flip()  # Atualiza a tela

        # Eventos do Pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        clock.tick(60)

    pygame.quit()
    print("Evolução concluída.")


if __name__ == '__main__':
    iniciar()
