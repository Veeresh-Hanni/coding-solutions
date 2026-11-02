# Write your MySQL query statement below
-- SELECT ROUND(SUM(tiv_2016), 2) as tiv_2016
-- FROM Insurance
-- WHERE tiv_2015 IN (
--     SELECT tiv_2015 
--     FROM Insurance 
--     GROUP BY tiv_2015 
--     HAVING COUNT(*) > 1
-- )
-- AND (lat, lon) IN (
--     SELECT lat, lon 
--     FROM Insurance 
--     GROUP BY lat, lon 
--     HAVING COUNT(*) = 1
-- );

WITH common_tiv_2015 AS (
    SELECT tiv_2015 
    FROM Insurance 
    GROUP BY tiv_2015 
    HAVING COUNT(*) > 1
), 
unique_lat_lon AS(
    SELECT lat,lon
    FROM Insurance
    GROUP BY lat,lon
    HAVING COUNT(pid) = 1)

SELECT ROUND(SUM(tiv_2016), 2) as tiv_2016
FROM Insurance i
JOIN common_tiv_2015 ct ON i.tiv_2015 = ct.tiv_2015
JOIN unique_lat_lon ul ON i.lat = ul.lat AND i.lon = ul.lon;