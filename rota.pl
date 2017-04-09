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
route(Place1, PLace2, Day, [Flight_num/Dep_time/Arr_time]):-flight(Place1,PLace2,Day,Flight_num,Dep_time,Arr_time).
route(Place1, PLace2, Day, Route):-route_r(Place1,PLace2,Day,Route,[Place1]).

/*parte recursiva da função*/
route_r(PLace2,PLace2,Day,Route,Visited).
route_r(Place1,PLace2,Day,Route,Visited):-
  flight(Place1,Aux,Day,Flight_num,Dep_time,Arr_time),
  \+ member(Aux,Visited),
  route_r(Aux,PLace2,Day,RouteAux,[Aux|Visited]),
  approve([Aux/PLace1/Dep_time/Arr_time],RouteAux),
  append([Aux/PLace1/Dep_time/Arr_time],RouteAux,Route).

/* ver esta função parece muito aldrabada */
  approve([_]).
  approve([]).
  approve([_/_/Dep_time1/Arr_time1],[_/_/Dep_time2:Arr_time2|_]):-transfer(Arr_time1,Dep_time2).

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
