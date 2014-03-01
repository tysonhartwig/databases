/* Problem 4

Find names and grades of students who only have friends in the same grade. Return the result sorted by grade, then by name within each grade. */

select grade, name 
from   Highschooler 
where  Highschooler.ID not in(
     select H1.ID
     from Highschooler H1, Friend, Highschooler H2
     where H1.ID   = Friend.ID1
     and   H2.ID   = Friend.ID2
     and   H1.grade <> H2.grade)
order by grade, name;

