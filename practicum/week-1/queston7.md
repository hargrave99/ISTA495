Write a SQL solution to output the 10 least dense countries.

select country
from world
WHERE (area > 0)
order by (population/area)
asc
limit 10