Write a SQL solution to output the 10 most dense countries.

select country
from world
WHERE (area > 0)
order by (population/area)
desc
limit 10