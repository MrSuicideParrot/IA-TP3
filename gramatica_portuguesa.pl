
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
sentenca(sentenca(N,V)) --> frase_nom(N), frase_ver(V)
sentenca(sentenca(NP,VP)) --> frase_nom_p(NP), frase_ver_p(VP)

%Nome  artigo ou nome -- Tudo no singular
frase_nom(frase_nom(Nome)) --> nome_m(Nome)
frase_nom(frase_nom(Nome)) --> nome_f(Nome)

frase_nom(frase_nom(Artigo, Nome)) --> nome_m(Nome), artigo_m(Artigo)
frase_nom(frase_nom(Artigo, Nome)) --> nome_f(Nome), artigo_f(Artigo)

%Nome artigo ou nome -- Tudo Plural
frase_nom_p(frase_nom_p(Nome)) --> nome_p_m(Nome)
frase_nom_p(frase_nom_p(Nome)) --> nome_p_f(Nome)

frase_nom_p(frase_nom_p(Artigo, Nome)) --> nome_p_m(Nome), artigo_p_m(Artigo)
frase_nom_p(frase_nom_p(Artigo, Nome)) --> nome_p_f(Nome), artigo_p_f(Artigo)

%Verbo singular
frase_ver(frase_ver(Verbo,Resto)) --> verbo(Verbo), frase_nom(Resto)
frase_ver(frase_ver(Verbo,Resto)) --> verbo(Verbo), frase_nom_p(Resto)
frase_ver(frase_ver(Verbo)) --> verbo(Verbo)

%Verbo plural
frase_ver_p(frase_ver_p(Verbo,Resto)) --> verbo_p(Verbo), frase_nom(Resto)
frase_ver_p(frase_ver_p(Verbo,Resto)) --> verbo_p(Verbo), frase_nom_p(Resto)
frase_ver_p(frase_ver_p(Verbo)) --> verbo_p(Verbo)
