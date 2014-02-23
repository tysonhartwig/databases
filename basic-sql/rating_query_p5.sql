select name, title, stars, ratingDate 
from Movie natural join Reviewer natural join Rating 
order by name, title, stars desc;
