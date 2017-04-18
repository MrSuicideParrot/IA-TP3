# **Comparação entre ProLog e outras linguagens**
## *Inteligência Artificial - 2017*
#### 1º Problema - Planeador de viagens
Metodos para responder as seguintes questões:
1. Conseguir dizer em que dias é que existem ligações diretas entre dois aeroportos;
2. Conseguir dizer quais são os voos que temos de apanhar num determinado dia para conseguir ir de um aeroporto para outro, sendo que não seja necessário existir uma ligação direta e que exista um tempo para transferência entre voos de pelo menos 40 minutos;
3. Planear uma percurso com inicio e fim na mesma cidade, é necessário que nessa rota passemos por determinados pontos mo entanto, só podemos apanhar um voo por dia, a data de inicio e fim do percurso é dado pelo utilizador.   

###### **_ProLog_**
1.
  ````ProLog
    flight(Place1,PLace2,Day,Flight_num,Dep_time,Arr_time).
  ````
  * Place1 = Local de partida.
  * PLace2 = Local de chegada.
  * Day = Dia. (Variável)
  * Flight_num = Número do voo. (Variável)
  * Dep_time = Hora de partida. (Variável)
  * Arr_time = Hora de chegada. (Variável)

2.
````ProLog
  route(Place1, PLace2, Day, Route).
````
 * Place1 = Local de partida.
 * PLace2 = Local de chegada.
 * Day = Dia.
 * Roue = Rota a tomar. (Variável)

3.
````ProLog
  percurso(CidadeInicial, Pontos, Day1, Day2,Percurso).
````
  * CidadeInicial = Aeroporto onde o percurso é iniciado.
  * Pontos = Lista de aeroportos por onde é necessário passar.
  * Day1 = Dia do inicio do percurso.
  * Day2 = Dia do fim do percurso.
  * Percurso = Percurso planeado. (Variável)

###### **_Python_**
A implementação em Python apresenta um menu que o guia ao longo das queries que pretende efetuar, num dos passos desse menu poderá escolher que tipo de questão pretende efetuar.
###### Modo de utilização
````Bash
  $ python3 rota.py
````

#### 2º Problema - Gramática portuguesa
