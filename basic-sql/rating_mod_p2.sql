/*
Problem 2

Insert 5-star ratings by James Cameron for all movies in the database. Leave the review date as NULL.
*/

insert into Rating (rID, mID, stars)
select '207', Movie.mID, '5'
from Movie;

