Write a SQL solution to output all countries that either have an area bigger than 2 million square km or a population of more than 30 million. The solution should output 
only the followings: country, population and area.
<<<<<<< HEAD
=======

>>>>>>> 65416cab113314547d7b8a86e7d6d74295c13454

SELECT country, population, area FROM world WHERE (area > 2000000) OR (population > 30000000);

