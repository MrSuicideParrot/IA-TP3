/* o operador / tem precedencia 400*/
:- op(50,xfy,:).

/*utilização do member */
:- use_module(library(lists)).

/*consult(times).*/
open('times.pl', read, Str).
read_file(Str,Lines).
close(Str).
assert(Lines).

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
  not member(Aux,Visited),
  route_r(Aux,PLace2,Day,AuxRoute,[Aux|Visited]),
  approve([Aux/PLace1/Dep_time/Arr_time],Route),
  append([Aux/PLace1/Dep_time/Arr_time],Route,Route).

/* ver esta função parece muito aldrabada */
  approve([_/_/Dep_time1/Arr_time1],[]).
  approve([_/_/Dep_time1/Arr_time1],[_/_/Dep_time2:Arr_time2|_]):-transfer(Arr_time1,Dep_time2).
