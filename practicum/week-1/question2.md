Write a SQL solution to output all countries that either have an area bigger than 2 million square km or a population of more than 30 million. The solution should output 
only the followings: country, population and area.

SELECT country, population, area FROM world WHERE (area > 2000000) OR (population > 30000000);

