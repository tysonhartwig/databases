/* Problem 1

It's time for the seniors to graduate. Remove all 12th graders from Highschooler.
This operation will orphan the students Likes and friends*/

delete from Highschooler
where  grade = 12;

