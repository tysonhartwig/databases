/*  Problem 8

List movie titles and average ratings, from highest-rated to lowest-rated. If two or more movies have the same average rating, list them in alphabetical order.
*/

select Movie.title, avg(Rating.stars) as "Avg Rating"
from   Movie, Rating
where  Movie.mID = Rating.mID
group  by Movie.title
order  by avg(Rating.stars) desc, Movie.title;

