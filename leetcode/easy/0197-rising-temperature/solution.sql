# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
WHERE w1.temperature > w2.temperature;

-- SELECT id
-- FROM (
--     SELECT id,
--            recordDate,
--            temperature,
--            LAG(temperature) OVER (
--                ORDER BY recordDate
--            ) AS previous_temperature,
--            LAG(recordDate) OVER (
--                ORDER BY recordDate
--            ) AS previous_date
--     FROM Weather
-- ) w
-- WHERE temperature > previous_temperature
--   AND recordDate = previous_date + INTERVAL 1 DAY;