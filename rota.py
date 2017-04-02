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


# incio do script em si
def create_percurso(n):
    n = n.split('(')
    print(n)
    print(len(n))
    n = n[1]
    n = n.split(',',maxsplit=2)
    tempos[n[0]] = Percursos(n[0],n[1])
    rotas = n[2]
    rotas = rotas.replace(')', '')
    rotas = rotas[1:-2].split('/')
    while not rotas:
        print(rotas)

        #casos diferentes
        if x[0] == '[':
            print(x)
            x = x[1:]
        if x[-1] == '[':
            x = x[-1]

        #lista tratamento normal
        x = x.split(',')
        print(x)
     #   tempos[n[0]].viagens.append(Carreiras(*x))



tempos = {}

with open('times.pl','r') as fd:
    buffer = fd.read().replace('\n','').split('.')
    for n in buffer:
        create_percurso(n)


