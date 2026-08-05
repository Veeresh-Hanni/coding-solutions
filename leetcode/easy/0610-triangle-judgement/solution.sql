# Write your MySQL query statement below

-- SELECT *,
--     CASE 
--         WHEN x + y > z AND x + z > y AND y + z > x THEN "Yes" 
--         ELSE "No"
--     END as triangle
-- FROM Triangle;

SELECT 
    *, 
    IF(x + y > z AND y + z > x AND  x + z > y, "Yes", "No") AS triangle 
FROM 
    Triangle;