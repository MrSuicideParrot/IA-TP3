

class Carreiras:
    def __init__(self,data_Inicio, data_Fim, numeroID, dias):
        self.data_Inicio = data_Inicio
        self.data_Fim = data_Fim
        self.numeroID = numeroID
        if dias == 'alldays':
            self.dias = ['mo','tu','we', 'th', 'fr', 'sa','su']
        else:
            pass

class Percursos:
    def __init__(self,partida,fim):
        self.partida = partida
        self.fim = fim
        self.viagens = []


