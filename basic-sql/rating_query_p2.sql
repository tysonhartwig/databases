/* Problem 2

Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. */
select year 
from Movie natural join Rating 
where stars >= 4 
order by year;
