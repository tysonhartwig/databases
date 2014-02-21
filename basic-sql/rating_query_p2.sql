select year 
from Movie natural join Rating 
where stars >= 4 
order by year;
