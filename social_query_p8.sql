/*  Problem 8

Find the difference between the number of students in the school and the number of different first names. */

select count(*)
from   Highschooler H1, Highschooler H2
where  H1.name = H2.name
and    H1.ID   > H2.ID;

