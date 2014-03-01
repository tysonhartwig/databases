/* Problem 7

For each student A who likes a student B where the two are not friends, find if they have a friend C in common (who can introduce them!). For all such trios, return the name and grade of A, B, and C. */

select A.name, A.grade, B.name, B.grade, C.name, C.grade   
from Highschooler A, Friend F1, Highschooler B, Friend F2, Highschooler C, Likes
where A.ID  <> F2.ID2   
and   B.ID  <> F1.ID2   
and   B.ID  <> A.ID    
and   A.ID  =  F1.ID1    
and   B.ID  =  F2.ID1    
and   C.ID  =  F1.ID2    
and   C.ID  =  F2.ID2
and   A.ID  =  Likes.ID1
and   B.ID  =  Likes.ID2;

