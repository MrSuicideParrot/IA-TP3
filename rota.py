from pyparsing import Word, alphas, Literal, Suppress, Optional, nums, alphanums, OneOrMore


class Carreiras:
    def __init__(self,data_Inicio, data_Fim, numeroID, dias):
        diasPars = OneOrMore(Word(alphas) + Optional(Suppress(',')))
        self.data_Inicio = Tempo(data_Inicio)
        self.data_Fim = Tempo(data_Fim)
        self.numeroID = numeroID
        if dias == 'alldays':
            self.dias = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
        else:
            self.dias = diasPars.parseString(dias)


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


class Arvore:
    def __init__(self, nos):
        self.nodes = nos
        self.edges = [[False for _ in range(len(nos))] for _ in range(len(nos))]
        for j in range(len(nos)):
            self.edges[j][findIndex(nos[j].fim, nos)] = True


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
    while not (buffer == [''] or buffer):
        aux = firstLine.parseString(buffer[0])
        tempo.append(Percursos(aux[1], aux[2]))
        del buffer[0]
        while not buffer[0] == '':
            buffer[0] = buffer[0].replace(' ','')
            print(buffer[0])
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