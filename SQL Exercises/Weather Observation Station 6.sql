SELECT DISTINCT CITY FROM STATION
    WHERE (CITY LIKE 'a%' OR CITY LIKE 'e%' OR CITY LIKE 'i%' OR CITY LIKE 'o%' OR CITY LIKE 'u%');

SELECT DISTINCT CITY FROM STATION
    WHERE CITY REGEXP '^[aeiou]';

/* LIKE determines whether a string matches a specified pattern */
/* It was more interesting to use REGEX to obtain a Regex in MySQL to be able to search in a better way */
