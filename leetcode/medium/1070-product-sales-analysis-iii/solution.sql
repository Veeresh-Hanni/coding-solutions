# Write your MySQL query statement below
SELECT t.product_id , t.year as first_year, t.quantity, t.price FROM (SELECT s.*, DENSE_RANK() OVER (PARTITION BY s.product_id ORDER BY s.year) as dnk FROM Sales s) as t
WHERE dnk = 1; 