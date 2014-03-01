/* Problem 9

What is the average number of friends per student? (Your result should be just one number.) */

select avg(count)
from(
    select count(ID2) as count
    from   Friend
    group  by ID1);

