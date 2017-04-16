from sys import argv

nomeM = ['cacador', 'cachorro', 'rio', 'mar', 'tempo', 'sino', 'vento', 'martelo', 'tambor', 'tempo','rosto']
nomeF = ['menina','noticia', 'floresta','porta','vida','mae','cidade']

nomePM = ['lobos','tambores']
nomePF = ['meninas','lagrimas']

verboS = ['corre','correu','bateu']
verboP = ['corriam', 'bateram','correram']
preposicao = ['para', 'com']

contracaoM = ['no','pelo']
contracaoF = ['na','pela']

contracaoPM = ['nos','pelos']
contracaoPF = ['nas','pelas']

artigoF = ['a','A']
artigoM = ['o','O']

artigoPM = ['os','Os']
artigoPF = ['as','As']

carta = {'nomeM':['artigoM','contracaoM'],'nomeF':['artigoF','contracaoF'],'nomePM':['artigoPM','contracaoPM'],'nomePF':['artigoPF','contracaoPF']}

def preparaString(frase_raw):
    frase_preparada = frase_raw
    tipos = []
    for i in frase_preparada:
        if i in preposicao:
            tipos.append('preposicao')
        elif i in contracaoM:
            tipos.append('contracaoM')
        elif i in contracaoF:
            tipos.append('contracaoF')
        elif i in contracaoPM:
            tipos.append('contracaoPM')
        elif i in contracaoPF:
            tipos.append('contracaoPF')
        elif i in artigoM:
            tipos.append('artigoM')
        elif i in artigoF:
            tipos.append('artigoF')
        elif i in artigoPM:
            tipos.append('artigoPM')
        elif i in artigoPF:
            tipos.append('artigoPF')
        elif i in verboS:
            tipos.append('verboS')
        elif i in verboP:
            tipos.append('verboP')
        elif i in nomeM:
            tipos.append('nomeM')
        elif i in nomeF:
            tipos.append('nomeF')
        elif i in nomePM:
            tipos.append('nomePM')
        elif i in nomePF:
            tipos.append('nomePF')
        else:
            raise ValueError('Nome não identificado!')
    return frase_preparada, tipos


def fraseNomial(componentes,tipo, generic=0):
    if generic == 0:
        targets = ['nomeM','nomeF','nomePM','nomePF']
        for i in range(4):
            num, ret = r_fraseNomial(componentes,tipo,targets[i])
            if num != 0 and i < 2:
                return num, ret, 's'
            elif num != 0:
                return num, ret, 'p'
        return 0, None, None
    else:
        if generic == 1:
            for i in ['nomeM','nomeF']:
                num, ret = r_fraseNomial(componentes, tipo, i)
                if num != 0:
                    return num, ret, None
            return 0, None, None
        else:
            for i in ['nomePM','nomePF']:
                num, ret = r_fraseNomial(componentes, tipo, i)
                if num != 0:
                    return num, ret, None
            return 0, None, None


def r_fraseNomial(componentes,tipo,target):
    global carta
    teste = carta[target][0]
    if tipo[0] == target:
        return 1, 'fraseNominal(nome('+componentes[0]+')'')'
    elif len(componentes) >= 2 and tipo[0] == carta[target][0] and tipo[1] == target:
        return 2, 'fraseNominal(artigo('+componentes[0]+')nome('+componentes[1]+'))'
    elif len(componentes) >= 2 and tipo[0] == carta[target][1] and tipo[1] == target:
        return 2, 'fraseNominal(contracao(' + componentes[0] + ')nome(' + componentes[1] + '))'
    else:
        return 0, None


def frasePreposicional(componentes, tipos):
    if tipos[0] == 'preposicao':
        num, ret, _ = fraseNomial(componentes[1:],tipos[1:])
        if num == 0:
            raise ValueError('Frase incorreta!')
        return 1+num, 'frasePreposicional(preposicao('+componentes[0]+')'+ret+')'
    else:
        return 0, None

def fraseVerbal(componentes, tipos, type):
    if type == 's':
        flag = 1 # singular
        target = 'verboS'
    else:
        flag = 2 # plural
        target = 'verboP'

    if tipos[0] == target:
        if len(componentes)>1:
            num, ret, _ = fraseNomial(componentes[1:],tipos[1:],flag)
            if num != 0:
                return 1 + num, 'fraseVerbal(verbo(' + componentes[0] + ')' + ret + ')'
            else:
                num, ret = frasePreposicional(componentes[1:], tipos[1:])
                if num != 0:
                    return 1+num, 'fraseVerbal(verbo(' + componentes[0] + ')'+ret+')'
                else:
                    return 1, 'fraseVerbal(verbo('+componentes[0]+'))'
        else:
            return 1, 'fraseVerbal(verbo(' + componentes[0] + '))'
    else:
        return 0, None


componentes, tipos = preparaString(argv[1:])

'''Sentença'''
num , ret, flag = fraseNomial(componentes, tipos)
if num == 0:
    raise ValueError('Frase incorreta!')
resultado = ret

num, ret = fraseVerbal(componentes[num:],tipos[num:], flag)
if num == 0:
    raise ValueError('Frase incorreta!')
print('sent('+resultado+ret+')')