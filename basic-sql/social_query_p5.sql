/* Problem 5

Find the name and grade of all students who are liked by more than one other student. */

select   name, grade
from     Highschooler, Likes
where    Highschooler.ID = Likes.ID2
group by Highschooler.ID
having   count(Likes.ID1) > 1;

