from pyparsing import Word, alphas, Literal, Suppress, Optional, nums, alphanums, OneOrMore
#import argparse
from copy import copy

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
        return self.numeroID+"["+self.data_Inicio.__str__()+","+self.data_Fim.__str__()+']'


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
        if t1.horas == t2.horas:
            return t2.minutos-t1.minutos >= 40
        if t2.horas-t1.horas <= 1:
            return (60 - t1.minutos) + t2.minutos >= 40
        elif 0 >= t2.horas-t1.horas:
            return False
        else:
            return True

    def __str__(self):
        return str(self.horas)+':'+str(self.minutos)

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

        '''Criacao do dicionario reverso'''
        self.rev_dicionario = dict((v,k) for k,v in self.dicionario.items())

        self.edges = [[None for _ in range(len(self.dicionario))] for _ in range(len(self.dicionario))]
        self.edgesVeracidade = [True for _ in range(len(self.dicionario))]  #usra como o valor de True como ainda nao visitado

        for aux in nos:
            posicINI = self.dicionario[aux.partida]
            posicFIM = self.dicionario[aux.fim]
            self.edges[posicINI][posicFIM] = aux.viagens

    def search(self, partida, destino, day, direct=False):
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
            return [partida+"-"+destino+":"+resposta]

        if not direct:
            '''Voo indireto usando dfs'''
            self.edgesVeracidade[startIndex] = False
            return self.dfs(partida=startIndex, destino=endIndex, day=day)
        else:
            return None

    def dfs(self, partida, destino, day, hchegada=None, rota=[]):
        '''Caso de paragem'''
        if partida == destino:
            return []

        for i in range(len(self.dicionario)):
            if self.edgesVeracidade[i]:
                self.edgesVeracidade[i] = False
                if self.edges[partida][i] is not None:
                    for aux in self.edges[partida][i]:
                        if day in aux.dias and (hchegada is None or hchegada.transfer(aux.data_Inicio)):
                            resAux=self.dfs(i, destino, day, aux.data_Fim, rota)
                            if resAux is not None:
                                return [self.rev_dicionario[partida]+'-'+self.rev_dicionario[i]+':'+aux.__str__()].append(resAux)
                self.edgesVeracidade[i] = True
        return None

    '''Efetua consulta na base de dados para saber em que dias e que existem voos diretos'''
    def consulta(self, partida, destino):
        startIndex = self.dicionario[partida]
        endIndex = self.dicionario[destino]
        dicionarioL = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
        usedDays = [False for _ in range(7)]

        for aux in self.edges[startIndex][endIndex]:
            for x in aux:
                usedDays[dicionarioL.index(x)] = True

        print([dicionarioL[index] for index in range(7) if usedDays[index]])

    '''Roteiro de varios dias'''
    def iniciarRoteiro(self,start, aeroportos, diaInicio, diaFim):
        '''Tradução de cenas'''
        aeroportosNum = [self.dicionario[i] for i in aeroportos]
        startNum = self.dicionario[start]
        self.edgesVeracidade[startNum] = False
        return self.r_roteiro(startNum,aeroportosNum,startNum,diaInicio,self.counterDay(diaFim))

    def r_roteiro(self,start,aerportos,fim,diaInicio, diaFim):
        if diaFim <= 0:
            return  None

        if not aerportos:
            return self.search(start,fim,diaInicio,True)
        else:
            for i in range(len(self.dicionario)):
                if self.edgesVeracidade[i]:
                    if i in aerportos:
                        self.edgesVeracidade[i] = False
                        resultado1 = self.search(start,i,diaInicio,True)
                        if resultado1 is not None:
                            resultado2 = self.r_roteiro(i,self.arraySubtractor(aerportos,i),fim,self.nextDay(diaInicio),diaFim-1)
                            if resultado2 is not None:
                                return resultado1.append(resultado2)
                        self.edgesVeracidade[i] = True
            return self.r_roteiro(start,aerportos,fim,self.nextDay(diaInicio), diaFim)

    '''Retorna o dia a seguir'''
    def nextDay(day):
        dias = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
        return dias[(8+dias.index(day))%7]

    '''calcula o número máximo de viagens'''
    def counterDay(dayI, dayF):
        dias = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
        startIndex = dias.index(dayI)
        endIndex = dias.index(dayF)
        count = 0
        while startIndex != endIndex:
            startIndex = (8 + startIndex)%7
            count += 1
        return count

    '''Uma copia do array sme um determinado elemento'''
    def arraySubtractor( array, item):
        aux = copy(array)
        return aux.remove(item)






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
        index_tempo += 1

    return tempo


def findIndex(target, array):
    for i in range(len(array)):
        if array[i].partida == target:
            return i
    raise Exception('Valor não se encontrava no array!')

def main():
    connects = Arvore(readFile())
    opc = int(input('Selecione o tipo de query que pretende:\n1 - Rota\n2 - Iniciar roteiro\n3 - Todos os dias onde existem voos diretos\n'))
    if opc == 1:
        # search(self, partida, destino, day,
        day_ini = input('Insira o cidade inicial:')
        day_fin = input('Insira o cidade final:')
        day = input('Insira o dia onde pretende fazer a query:')
        print(connects.search(day_ini,day_fin,day))

    elif opc == 2:
        cid_ini = input('Insira o aeroporto inicial:')
        list = input('Insira as varias cidade separadas por espaços')
        day_ini = input('Insira o dia inicial:')
        day_fin = input('Insira o dia final:')
        print(connects.iniciarRoteiro(cid_ini,list.split(),day_ini,day_fin))

    elif opc == 3:
        day_ini = input('Insira o dia inicial:')
        day_fin = input('Insira o dia final:')
        print(connects.consulta(day_ini, day_fin))



if __name__ == '__main__':
    main()
