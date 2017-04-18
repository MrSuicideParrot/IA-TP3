/* o operador / tem precedencia 400*/
:- op(50,xfy,:).

/*utilização do member */
:- use_module(library(lists)).

transfer(Ho1:Min1,Ho2:Min2):-
  (Min2 - Min1) + (Ho2 - Ho1)*60 >= 40.

/*deptime(Route,Time):- */

flight(Place1,PLace2,Day,Flight_num,Dep_time,Arr_time):-
  timetable(Place1,PLace2,Horario),
  member(Dep_time/Arr_time/Flight_num/Days, Horario),
  verificaHora(Day, Days).

/*partimos de príncipio que o nome do dia está correto*/
verificaHora(Day,Days):-Days = alldays.
verificaHora(Day,Days):-member(Day,Days).

/*criador da rota entre um determinado ponto*/
route(Place1, PLace2, Day, Route):-route_r(Place1,PLace2,Day,Route,[Place1]).

/*parte recursiva da função*/
route_r(Place1, PLace2, Day, [Place1-PLace2:Flight_num:Dep_time:Arr_time],Visited):-flight(Place1,PLace2,Day,Flight_num,Dep_time,Arr_time).
route_r(Place1,PLace2,Day,Route,Visited):-
  flight(Place1,Aux,Day,Flight_num,Dep_time,Arr_time),
  \+ member(Aux,Visited),
  route_r(Aux,PLace2,Day,RouteAux,[Aux|Visited]),
  approve([PLace1-Aux:Flight_num:Dep_time:Arr_time],RouteAux),
  append([PLace1-Aux:Flight_num:Dep_time:Arr_time],RouteAux,Route).

/* ver esta função parece muito aldrabada */
approve([_]).
approve([]).
approve([_-_:_:Dep_time1:Arr_time1],[_-_:_:Dep_time2:Arr_time2|_]):-transfer(Arr_time1,Dep_time2).

/* Inicio do percurso */
percurso(CidadeInicial, Pontos, Day1, Day2,Percurso):-
  last(Pontos,Aux),
  CidadeInicial = Aux,
  false.

percurso(CidadeInicial, Pontos, Day1, Day2,[CidadeInicial-Aux:Day1:Flight_num:Dep_time:Arr_time|PercRest]):-
  %last(Pontos,Target),
  member(Aux,Pontos),
  flight(CidadeInicial,Aux, Day1, Flight_num,Dep_time,Arr_time),
  nextDay(Day1,Next),
  delete(Pontos,Aux,PontosAuxiliares),
  percurso_r(Aux, PontosAuxiliares, CidadeInicial, Next, Day2, PercRest).

percurso_r(CidadeInicial, [],Target, Day1, Day2,[CidadeInicial-Target:Day1:Flight_num:Dep_time:Arr_time]):-
  verifcaDia(Day1,Day2),
  flight(CidadeInicial,Target, Day2, Flight_num,Dep_time,Arr_time).

percurso_r(CidadeInicial, Pontos, Target, Day1, Day2,Percurso):-
  member(Aux,Pontos),
  verifcaDia(Day1,Day2),
  flight(CidadeInicial,Aux, Day1, Flight_num,Dep_time,Arr_time),
  nextDay(Day1, Next),
  delete(Pontos,Aux, PontosAuxiliares),
  percurso_r(Aux, PontosAuxiliares, Target, Next, Day2, PercRest),
  append([CidadeInicial-Aux:Day1:Flight_num:Dep_time:Arr_time],PercRest,Percurso).

percurso_r(CidadeInicial, Pontos, Target, Day1, Day2,Percurso):-
  nextDay(Day1, Next),
  verifcaDia(Next,Day2),
  percurso_r(CidadeInicial, Pontos, Target, Next, Day2,Percurso).

/*verifcar dia  valido */
verifcaDia(Day1,Day2):-
  nth1(Index1,[mo,tu,we,th,fr,sa,su],Day1),
  nth1(Index2,[mo,tu,we,th,fr,sa,su],Day2),
  Index1 =< Index2.

/*Calculo do dia a seguir */
nextDay(mo, tu).
nextDay(tu, we).
nextDay(we, th).
nextDay(th, fr).
nextDay(fr, sa).
nextDay(sa, su).
nextDay(su, mo).



timetable(edinburgh,london,
[ 9:40/10:50/ba4733/alldays,
13:40/14:50/ba4773/alldays,
19:40/20:50/ba4833/[mo,tu,we,th,fr,su]]).

timetable(london,edinburgh,
[ 9:40/10:50/ba4732/alldays,
11:40/12:50/ba4752/alldays,
18:40/19:50/ba4822/[mo,tu,we,th,fr]]).

timetable(london,ljubljana,
[13:20/16:20/ju201/[fr],
13:20/16:20/ju213/[su]]).

timetable(london,zurich,
[ 9:10/11:45/ba614/alldays,
14:45/17:20/sr805/alldays]).

timetable(london,milan,
[ 8:30/11:20/ba510/alldays,
11:00/13:50/az459/alldays]).

timetable(ljubljana,zurich,
[11:30/12:40/ju322/[tu,th]]).

timetable(ljubljana,london,
[11:10/12:20/yu200/[fr],
11:25/12:20/yu212/[su]]).

timetable(milan,london,
[ 9:10/10:00/az458/alldays,
12:20/13:10/ba511/alldays]).

timetable(milan,zurich,
[ 9:25/10:15/sr621/alldays,
12:45/13:35/sr623/alldays]).

timetable(zurich,ljubljana,
[13:30/14:40/yu323/[tu,th]]).

timetable(zurich,london,
[ 9:00/9:40/ba613/[mo,tu,we,th,fr,sa],
16:10/16:55/sr806/[mo,tu,we,th,fr,su]]).

timetable(zurich,milan,
[ 7:55/8:45/sr620/alldays]).
