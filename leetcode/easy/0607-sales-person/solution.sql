# Write your MySQL query statement below



SELECT s.sales_id from SalesPerson s
JOIN Orders o ON s.sales_id = o.sales_id
Join Company c ON c.com_id= o.com_id
WHERE c.name = 'RED'
 