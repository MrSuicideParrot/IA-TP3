
/*
sentenca --> noun_phrase, verbal_phrase.
sentenca --> noun_phrase_p, verbal_phrase_p.

frase_nom --> determiner_f, noun_f.
frase_nom --> determiner_m, noun_m.
frase_nom --> noun_f.
frase_nom --> noun_m.

frase_nom_p --> determiner_p_f, noun_p_f.
frase_nom_p --> determiner_p_m, noun_p_m.
frase_nom_p --> noun_p_f.
frase_nom_p --> noun_p_m.
*/

%Nome e verbo
sentenca(sentenca(N,V)) --> frase_nom(N), frase_ver(V).
sentenca(sentenca(NP,VP)) --> frase_nom_p(NP), frase_ver_p(VP).

%Nome  artigo ou nome -- Tudo no singular
frase_nom(frase_nom(Nome)) --> nome_m(Nome).
frase_nom(frase_nom(Nome)) --> nome_f(Nome).

frase_nom(frase_nom(Artigo, Nome)) --> artigo_m(Artigo), nome_m(Nome).
frase_nom(frase_nom(Artigo, Nome)) --> artigo_f(Artigo), nome_f(Nome).

frase_nom(frase_nom(Contra, Nome)) --> contracao_m(Contra), nome_m(Nome).
frase_nom(frase_nom(Contra, Nome)) --> contracao_f(Contra), nome_f(Nome).


%Nome artigo ou nome -- Tudo Plural
frase_nom_p(frase_nom_p(Nome)) --> nome_p_m(Nome).
frase_nom_p(frase_nom_p(Nome)) --> nome_p_f(Nome).

frase_nom_p(frase_nom_p(Artigo, Nome)) --> artigo_p_m(Artigo), nome_p_m(Nome).
frase_nom_p(frase_nom_p(Artigo, Nome)) --> artigo_p_f(Artigo), nome_p_f(Nome).

frase_nom_p(frase_nom_p(Contra, Nome)) --> contracao_p_m(Contra), nome_p_m(Nome).
frase_nom_p(frase_nom_p(Contra, Nome)) --> contracao_p_f(Contra), nome_p_f(Nome).

%Preposição
frase_prep(frase_prep(Preposi,Frase)) --> prep(Preposi), frase_nom(Frase).
frase_prep(frase_prep(Preposi,Frase)) --> prep(Preposi), frase_nom_p(Frase).

%Verbo singular
frase_ver(frase_ver(Verbo,Resto)) --> verbo(Verbo), frase_nom(Resto).
frase_ver(frase_ver(Verbo,Resto)) --> verbo(Verbo), frase_nom_p(Resto).
frase_ver_p(frase_ver_p(Verbo,Resto)) --> verbo(Verbo), frase_prep(Resto).
frase_ver(frase_ver(Verbo)) --> verbo(Verbo).

%Verbo plural
frase_ver_p(frase_ver_p(Verbo,Resto)) --> verbo_p(Verbo), frase_nom(Resto).
frase_ver_p(frase_ver_p(Verbo,Resto)) --> verbo_p(Verbo), frase_nom_p(Resto).
frase_ver_p(frase_ver_p(Verbo,Resto)) --> verbo_p(Verbo), frase_prep(Resto).
frase_ver_p(frase_ver_p(Verbo)) --> verbo_p(Verbo).

%Agora anar a fazer levantamentos de palavras

%nome masculino
nome_m(nome(cacador)) --> [cacador].
nome_m(nome(cachorro)) --> [cachorro].
nome_m(nome(rio)) --> [rio].
nome_m(nome(mar)) --> [mar].
nome_m(nome(tempo)) --> [tempo].
nome_m(nome(sino)) --> [sino].
nome_m(nome(vento)) --> [vento].
nome_m(nome(martelo)) --> [martelo].
nome_m(nome(tambor)) --> [tambor].
nome_m(nome(tempo)) --> [tempo].
nome_m(nome(rosto)) --> [rosto].

%nome femenino
nome_f(nome(menina)) --> [menina].
nome_f(nome(noticia)) --> [noticia].
nome_f(nome(floresta)) --> [floresta].
nome_f(nome(porta)) --> [porta].
nome_f(nome(vida)) --> [vida].
nome_f(nome(mae)) --> [mae].
nome_f(nome(cidade)) --> [cidade].

%plurais
nome_p_m(nome(lobos)) --> [lobos].
nome_p_m(nome(tambores)) --> [tambores].

nome_p_f(nome(meninas)) --> [meninas].
nome_p_f(nome(lagrimas)) --> [lagrimas].

%verbos
verbo(verbo(corre)) --> [corre].
verbo(verbo(correu)) --> [correu].
verbo(verbo(bateu)) --> [bateu].

verbo_p(verbo_p(corriam)) --> [corriam].
verbo_p(verbo_p(bateram)) --> [bateram].
verbo_p(verbo_p(correram)) --> [correram].

%preposicoes
prep(preposicao(para)) --> [para].
prep(preposicao(com)) --> [com].

%contracoes femininas
contracao_f(artigo(na)) --> [na].
contracao_f(artigo(pela)) --> [pela].


%contracoes masculinas
contracao_m(artigo(no)) --> [no].
contracao_m(artigo(pelo)) --> [pelo].

%plural
contracao_p_m(artigo(nos)) --> [nos].
contracao_p_m(artigo(pelos)) --> [pelos].

contracao_p_f(artigo(nas)) --> [nas].
contracao_p_f(artigo(pelas)) --> [pelas].

%artigo masculo
artigo_m(artigo(o)) --> [o].
artigo_m(artigo('O')) --> ['O'].

%artugo femenino
artigo_f(artigo(a)) --> [a].
artigo_f(artigo('A')) --> ['A'].

%plurais
artigo_p_m(artigo(os)) --> [os].
artigo_p_m(artigo('Os')) --> ['Os'].

artigo_p_f(artigo(as)) --> [as].
artigo_p_f(artigo('As')) --> ['As'].
