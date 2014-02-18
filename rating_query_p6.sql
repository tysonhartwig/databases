/*  Problem 6

For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie. */

select name, title
from Movie, Rating R1, Rating R2, Reviewer
where Reviewer.rID  = R1.rID
  and R1.rID	    = R2.rID
  and Movie.mID	    = R2.mID
  and R2.mID	    = R1.mID
  and R1.ratingDate > R2.ratingDate
  and R1.stars      > R2.stars;

