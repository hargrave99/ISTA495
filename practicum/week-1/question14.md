Which countries receive the most migrants? List the name and the migrants number of the top 10.

select country, migrants
from world
WHERE migrants IS NOT NULL
order by (migrants)
desc
limit 10