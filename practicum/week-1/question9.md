Write a SQL solution to output the land share of all the countries. 
Land share = land area divided by the population

SELECT country, (area/population::numeric) AS LandShare FROM world 