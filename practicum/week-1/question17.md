Which countries have a low population density, low fertility rate and hig migrants? List the top 10. 

SELECT country, (population / area) AS "PopulationDensity" FROM world WHERE (area > 0)
ORDER BY PopulationDensity asc
limit 10

select country, fertility
from world
WHERE (fertility > 0)
order by fertility
asc
limit 10

select country, migrants
from world
WHERE migrants IS NOT NULL
order by migrants
desc
limit 10