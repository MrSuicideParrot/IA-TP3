import argparse

nomes = ['cacador', 'cachorro', 'rio', 'mar', 'tempo', 'sino', 'vento', 'martelo', 'tambor', 'tempo','menina','noticia', 'floresta','porta','vida','mae','cidade','lobos','tambores','meninas','lagrimas']
verbos = ['corre','correu','bateu', 'corriam', 'bateram','correram']
preposicao = ['para', 'com']
contracao = ['no','pelo','na','pela']
artigo = ['a','A','o','O','as','As',]


def preparaString(frase_raw):
    frase_preparada = frase_raw.split()
    tipos = []
    for i in frase_preparada:
        if i in preposicao:
            tipos.append('preposicao')
        elif i in contracao:
            tipos.append('contracao')
        elif i in artigo:
            tipos.append('artigo')
        elif i in verbos:
            tipos.append('verbo')
        elif i in nomes:
            tipos.append('nome')
        else:
            raise ValueError('Nome não identificado!')
    return frase_preparada, tipos


def fraseNomial(componentes,tipo):
    if tipo[0] == 'nome':
        return 1, 'fraseNomial('+tipo[0]+'('+componentes[0]+')'')'
    elif tipo[0] == 'artigo' and tipo[1] == 'nome':
        return 2, 'fraseNomial(artigo('+componentes[0]+')nome('+componentes[1]+'))'
    elif tipo[0] == 'contracao' and tipo[1] == 'nome':
        return 2, 'fraseNomial(contracao(' + componentes[0] + ')nome(' + componentes[1] + '))'
    else:
        return 0, None


def frasePreposicional(componentes, tipos):
    if tipos[0] == 'preposicao':
        num, ret = fraseNomial(componentes[1:],tipos[1:])
        if num == 0:
            raise ValueError('Frase incorreta!')
        return 1+num, 'frasePreposicional(preposicao('+componentes[0]+')'+ret+')'
    else:
        return 0, None

def fraseVerbal(componentes, tipos):
    if tipos[0] == 'verbo':
        num, ret = fraseNomial(componentes[1:],tipos[1:])
        if num != 0:
            return 1 + num, 'fraseVerbal(verbo(' + componentes[0] + ')' + ret + ')'
        else:
            num, ret = frasePreposicional(componentes[1:], tipos[1:])
            if num != 0:
                return 1+num, 'fraseVerbal(verbo(' + componentes[0] + ')'+ret+')'
            else:
                return 1, 'fraseVerbal(verbo('+componentes[0]+'))'
    else:
        return 0, None

'''Parser do argv'''
parser = argparse.ArgumentParser(description='Verificador de gramática portuguesa.')
parser.add_argument('-f','--frase',type=str,help='String que pretende analisar')
args = parser.parse_args()

componentes, tipos = preparaString(args.frase)

'''Sentença'''
num , ret = fraseNomial(componentes, tipos)
if num == 0:
    raise ValueError('Frase incorreta!')
resultado = ret

num, ret = fraseVerbal(componentes[num:],tipos[num:])
if num == 0:
    raise ValueError('Frase incorreta!')
print('sent('+ret+resultado+')')