class DietaCommand:
    def __init__(self,
                 porcoes: int = 8,
                 calorias: int = 1500,
                 proteinas: int = 200,
                 lipidios: int = 20,
                 carboidratos: int = 200,
                 fibras: int = 200 ,
                 categorias=None):
        if categorias is None:
            categorias = [
                "Cereais",
                "Verduras",
                "Frutas",
                "Gorduras_Oleos",
                "Pescados",
                "Carnes",
                "Leites",
                "Bebidas",
                "Ovos",
                "Açucarados",
                "Miscelâneas",
                "Industrializados",
                "Preparados",
                "Leguminosas",
                "Nozes"
            ]
        self.porcoes = porcoes
        self.calorias = calorias
        self.proteinas = proteinas
        self.lipidios = lipidios
        self.carboidratos = carboidratos
        self.fibras = fibras
        self.categorias = categorias


