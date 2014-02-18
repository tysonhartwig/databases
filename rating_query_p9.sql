/*
Problem 9

Find the names of all reviewers who have contributed three or more ratings. (As an extra challenge, try writing the query without HAVING or without COUNT.) 
*/
select Reviewer.name 
from   Reviewer natural join Rating
group  by rID
having count(Rating.stars) >= 3;

