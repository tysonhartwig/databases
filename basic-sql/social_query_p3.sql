/*  Problem 3

For every pair of students who both like each other, return the name and grade of both students. Include each pair only once, with the two names in alphabetical order. */

select distinct H1.name, H1.grade, H2.name, H2.grade
from   Highschooler H1, Likes L1, Highschooler H2, Likes L2
where  H1.ID    = L1.ID1
and    L1.ID1   = L2.ID2
and    L1.ID2   = L2.ID1
and    H2.ID    = L2.ID1
and    H2.name >= H1.name;

