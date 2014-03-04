/*  Problem 6

Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. Sort by grade, then by name within each grade. */

select distinct grade, name
from   Highschooler
where  Highschooler.ID not in (
          select ID1
          from Likes
          union
          select ID2
          from Likes)
 order by grade, name;

