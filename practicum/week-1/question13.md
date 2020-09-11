Wich countries send the most migrants? List the top 10.

select country, migrants
from world
WHERE migrants IS NOT NULL
order by (migrants)
asc
limit 10