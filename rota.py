class carreiras:
    def __init__(self,data_Inicio, data_Fim, numeroID, dias):
        self.data_Inicio = data_Inicio
        self.data_Fim = data_Fim
        self.numeroID = numeroID

class percursos:
    def __init__(self,partida,fim,):
        self.partida = partida
        self.fim = fim
        self.viagens = []


# incio do script em si
def create_percurso(n):
    


tempos = {}

with open('times.pl','r') as fd:
    buffer = fd.read().replace('\n','').split('.')
    for n in buffer:
        create_percurso(n)


