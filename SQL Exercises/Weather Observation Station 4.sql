SELECT 
    COUNT(CITY) - COUNT(DISTINCT CITY) AS RESULT
FROM STATION;

/* You can select two things in a select and count using COUNT(). Making the necessary calculations between them */