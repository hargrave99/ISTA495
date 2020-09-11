Write a SQL solution to output the land share value of the wold (that is, the sum of the land area divided by the sum of the population).

SELECT SUM(area)/(SELECT SUM(population))::numeric AS WorldLandShare FROM world