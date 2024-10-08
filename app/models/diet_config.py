class DietaConfig:
    def __init__(self,
        tamanho_populacao: int = 3000,
        maximo_evolucoes: int = 150,
        elite_proporcao: float = 0.1,
        mutacao_proporcao: float = 0.05):

        self.tamanho_populacao = tamanho_populacao
        self.maximo_evolucoes = maximo_evolucoes
        self.elite_proporcao = elite_proporcao
        self.mutacao_proporcao = mutacao_proporcao
