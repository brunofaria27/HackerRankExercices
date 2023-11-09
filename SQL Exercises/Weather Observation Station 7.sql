/* MySQL Regex:  https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/ */

SELECT DISTINCT CITY FROM STATION
    WHERE CITY REGEXP '[aeiou]$';

SELECT DISTINCT CITY FROM STATION 
    WHERE (CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' OR CITY LIKE '%u');