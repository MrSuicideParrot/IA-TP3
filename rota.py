from pyparsing import Word, alphas, Literal

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

class Tempo:
    def __init__(self,horas,minutos):
        self.horas
        self.minutos

''' READING FILE'''
fd = open('times.pl','r')
buffer=fd.read()
buffer.split('\n')

'''Parsing lines'''

'''Diferentes tipos de parsers'''
firstLine = Literal('timetable') + '(' + Word(alphas) +',' + Word(alphas) + ',\n'
for line in buffer:
