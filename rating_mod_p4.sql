/* Problem 4

Remove all ratings where the movie's year is before 1970 or after 2000, and the rating is fewer than 4 stars.*/

delete from Rating
where  stars < 4
and    exists(
          select mID
          from   Movie
          where  Movie.mID = Rating.mID
          and( year < 1970
            or year > 2000));

