1. Download and install PostgreSQL database (it is available at https://www.postgresql.org)
2. Create a database and name it as ISTA495.practicum
3. Ctreat the following table:
  - table name: world
  - table columns: id, country, population, area, migrants,fertility,medianage,urbanpopulation (id is a number and it is the primary key, name and continent are strings, area and population are numbers)
4. Populate the world table using the csv file included in this folder

Hint:

* [How to import CSV file into PostgreSQL table](https://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/)

* [How to import a selected number of the columns of a csv file](https://stackoverflow.com/questions/12618232/copy-a-few-of-the-columns-of-a-csv-file-into-a-table/49906327)



create temporary table t(id integer, country text, population text, yearlychange text, netchange text, area text, migrants text, fertility text, medianage text, urbanpopulation text);
copy t
From 'C:\Users\seamu\OneDrive\Documents\Desktop\world.csv'
DELIMITER ',' 
CSV HEADER;
insert into world(id,country,population,area,migrants,fertility,medianage,urbanpopulation)
select id,country,population,area,migrants,fertility,medianage,urbanpopulation
from t;
drop table t;

![screenshot of table] (question1picture.png)