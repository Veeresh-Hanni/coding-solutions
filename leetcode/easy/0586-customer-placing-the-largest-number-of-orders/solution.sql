# Write your MySQL query statement below

-- SELECT customer_number
-- FROM Orders
-- GROUP BY customer_number
-- HAVING COUNT(order_number) = (
--     SELECT MAX(order_count)
--     FROM (
--         SELECT COUNT(order_number) AS order_count
--         FROM Orders
--         GROUP BY customer_number
--     ) AS temp
-- );

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;

-- WITH customer_orders AS (
--     SELECT
--         customer_number,
--         COUNT(order_number) AS total_orders
--     FROM Orders
--     GROUP BY customer_number
-- ),
-- ranked AS (
--     SELECT *,
--         DENSE_RANK() OVER (
--             ORDER BY total_orders DESC
--         ) AS rnk
--     FROM customer_orders
-- )
-- SELECT customer_number
-- FROM ranked
-- WHERE rnk = 1;