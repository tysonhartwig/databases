/*  Problem 7

For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. Sort by movie title. */

select distinct Movie.title, R1.stars
from   Movie 
       natural join Rating R1
       left outer join Rating R2
       on (R1.mID = R2.mID and R1.stars < R2.stars)
where  R2.stars is null
order  by Movie.title;

