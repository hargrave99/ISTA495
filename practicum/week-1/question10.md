Write a SQL solution to output the 10 countries who have the highest land share.

select country
from world
WHERE (area > 0)
order by (area/population)
desc
limit 10