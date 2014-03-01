/* Problem 2

For every student who likes someone 2 or more grades younger than themselves, return that student's name and grade, and the name and grade of the student they like. */
select H1.name, H1.grade, H2.name, H2.grade
from   Highschooler H1, Likes, Highschooler H2
where  H1.ID   = ID1
and    H2.ID   = ID2
and    H1.grade - H2.grade >= 2;

