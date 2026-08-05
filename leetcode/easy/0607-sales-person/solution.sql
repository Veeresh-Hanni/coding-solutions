# Write your MySQL query statement below

SELECT s.name FROM SalesPerson s
WHERE s.sales_id NOT IN (
    SELECT s.sales_id from SalesPerson s
    JOIN Orders o ON s.sales_id = o.sales_id
    Join Company c ON c.com_id= o.com_id
    WHERE c.name = 'RED'
    )