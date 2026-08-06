/*
Enter your query here.
*/


SELECT 
    ROUND((MAX(LAT_N) + MAX(LONG_W)) - (MIN(LAT_N) + MIN(LONG_W)),4)
    
FROM STATION;
