Write a SQL solution to output the population density (population per unit area) of all countries.

SELECT country, (population / area) AS "PopulationDensity" FROM world WHERE (area > 0) 