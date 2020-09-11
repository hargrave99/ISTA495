Which country has the highest medium age and lowest fertility rate?

SELECT country, medianage
FROM world
ORDER BY (medianage)
desc
limit 10

Japan has highest median age.

SELECT country, fertility
FROM world
WHERE (fertility >0)
ORDER BY (fertility)
asc
limit 10

South Korea has lowest fertility rate.