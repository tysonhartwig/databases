/*  Problem 1

Find the names of all students who are friends with someone named Gabriel. 
*/
select H2.name
from   Highschooler H1, Friend, Highschooler H2
where  H1.name = 'Gabriel'
and    H1.ID   = ID1
and    H2.ID   = ID2;

