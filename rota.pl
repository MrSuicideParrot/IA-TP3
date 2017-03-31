/* o operador / tem precedencia 400*/
:- op(50,xfy,:).
:- use_module(library(lists)).

/*consult(times).*/

transfer(Ho1:Min1,Ho2:Min2):-
  (Min2 - Min1) + (Ho2 - Ho1)*60 >= 40.

/*deptime(Route,Time):- */

flight(Place1,PLace2,Day,Flight_num,Dep_time,Arr_time):-
  timetable(Place1,PLace2,Horario),
  member(Dep_time/Arr_time/Flight_num/Days, Horario),
  verificaHora(Day, Days).

verificaHora(Day,Days):-Days = alldays.
verificaHora(Day,Days):-member(Day,Days).



/*isElement([Dep_time/Arr_time/Flight_num|Horario]):-*/
