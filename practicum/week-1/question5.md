Wite a SQL solution to output the population share (population of the country divided by the population of the world) of the countires.

SELECT country, (population/7794798739::numeric) AS PopulationShare FROM world 