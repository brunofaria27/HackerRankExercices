SELECT 
    CITY, LENGTH(CITY) AS SMALLER_CITIES
FROM STATION
    ORDER BY LENGTH(CITY), CITY ASC
LIMIT 1;

SELECT 
    CITY, LENGTH(CITY) AS BIGGEST_CITIES
FROM STATION
    ORDER BY LENGTH(CITY) DESC, CITY
LIMIT 1;

/* LIMIT 1 is used because it returns all cities with
   the character count using LENGTH(), LIMIT is used
   to be able to get only the first one according to the ordering */