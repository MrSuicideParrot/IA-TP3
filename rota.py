from pyparsing import Word, alphas, Literal, Suppress, Optional, nums, alphanums, OneOrMore
import argparse

class Carreiras:
    def __init__(self,data_Inicio, data_Fim, numeroID, dias):
        diasPars = OneOrMore(Word(alphas) + Optional(Suppress(',')))
        self.data_Inicio = Tempo(data_Inicio)
        self.data_Inicio = Tempo(data_Inicio)
        self.data_Fim = Tempo(data_Fim)
        self.numeroID = numeroID
        if dias == 'alldays':
            self.dias = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
        else:
            self.dias = diasPars.parseString(dias)

    def __str__(self):
        return self.numeroID+"/"+self.data_Inicio+"/"+self.data_Fim


class Percursos:
    def __init__(self, partida, fim):
        self.partida = partida
        self.fim = fim
        self.viagens = []


class Tempo:
    def __init__(self, tempo):
        tempoPars = Word(nums) + Suppress(':') + Word(nums)
        tempo = tempoPars.parseString(tempo)
        self.horas = int(tempo[0])
        self.minutos = int(tempo[1])

    def transfer(self,t2):
        t1 = self
        return (t2.horas - t1.horas)*60 + (t2.minutos - t1.minutos) <= 40

class Arvore:
    def __init__(self, nos):

        '''Criação de dicionario e organização'''
        self.dicionario = {}
        posic = 0
        for aux in nos:
            if aux.partida not in self.dicionario:
                self.dicionario[aux.partida] = posic
                posic += 1
            if aux.fim not in self.dicionario:
                self.dicionario[aux.fim] = posic
                posic += 1

        self.edges = [[None for _ in range(len(self.dicionario))] for _ in range(len(self.dicionario))]
        self.edgesVeracidade = [[False for _ in range(len(self.dicionario))] for _ in range(len(self.dicionario))] #usra como o valor de True como ainda nao visitado

        for aux in nos:
            posicINI = self.dicionario[aux.partida]
            posicFIM = self.dicionario[aux.fim]
            self.edges[posicINI][posicFIM] = aux.viagens
            self.edgesVeracidade[posicINI][posicFIM] = True

    def search(self, partida, destino, day):
        startIndex = self.dicionario[partida]
        endIndex = self.dicionario[destino]

        '''Caso exista um voo direto'''
        resposta = None
        try:
            for aux in self.edges[startIndex][endIndex]:
                if day in aux.dias:
                    resposta = aux.__str__()
        except TypeError:
            pass
        if resposta is not None:
            print(partida+"/"+destino+"/"+resposta)
            return

        '''Voo indireto usando dfs'''
        resposta = self.dfs(partida=startIndex, destino=endIndex, day=day)
        print(resposta)

    def dfs(self, partida, destino, day, hchegada=None, rota=[]):
        '''Caso de paragem'''
        if partida == destino:
            return []

        resAux = None
        for i in range(len(self.dicionario)):
            if self.edgesVeracidade[partida][i]:
                self.edgesVeracidade[partida][i] = False
                try:
                    for aux in self.edges[partida][i]:
                        if day in aux and (hchegada is None or hchegada.transfer(aux.data_Inicio)):
                            resAux=self.dfs(i, destino, day, aux.data_Fim, rota)
                            if resAux is not None:
                                return aux.__str__()+"/"+resAux
                except TypeError:
                    pass
            self.edgesVeracidade[partida][i] = True
        return None

def readFile():
    tempo = []
    ''' READING FILE'''
    fd = open('times.pl', 'r')
    buffer=fd.read().split('\n')
    '''Parsing lines'''

    '''Diferentes tipos de parsers'''
    firstLine = Literal('timetable') + Suppress('(') + Word(alphas) +Suppress(',') + Word(alphas) + Suppress(',')
    carreiraLine = Optional(Suppress('[')) + Word(nums+':'+nums) + Suppress('/') + Word(nums+':'+nums) + Suppress('/') + Word(alphanums) + Suppress('/') + (Literal('alldays') ^ (Suppress('[')+OneOrMore(Word(alphas+',')^Word(alphas))+Suppress(']'))) + (Suppress(']).') ^ Suppress(','))

    '''Inicio de parser'''
    i = 0
    index_tempo = 0
    while not (buffer == [''] or buffer == []):
        aux = firstLine.parseString(buffer[0])
        tempo.append(Percursos(aux[1], aux[2]))
        del buffer[0]
        while not buffer[0] == '':
            buffer[0] = buffer[0].replace(' ','')
            aux = carreiraLine.parseString(buffer[0])
            tempo[index_tempo].viagens.append(Carreiras(*aux))
            del buffer[0]
        del buffer[0]
        ++index_tempo

    return tempo


def findIndex(target, array):
    for i in range(len(array)):
        if array[i].partida == target:
            return i
    raise Exception('Valor não se encontrava no array!')

def main():
    '''Parser da linha de comandos'''
    parser = argparse.ArgumentParser(description='Programa de calculo de itenerário entre aeroportos.')
    parser.add_argument('-p','--partida', type=str, help='Aeroporto de partida')
    parser.add_argument('-d','--destino', type=str, help='Aeroporto de destino')
    parser.add_argument('--day', choices=['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su'],help='Dia onde pertende que a rota se aplique.')

    '''Inicio do script'''
    args = parser.parse_args()
    connects = Arvore(readFile())
    connects.search(args.partida, args.destino, args.day)

if __name__ == '__main__':
    main()