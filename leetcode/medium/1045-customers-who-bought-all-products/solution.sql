# Write your MySQL query statement below
SELECT customer_id from Customer
GROUP BY customer_id 
HAVING COUNT(*) = (
    SELECT COUNT(p.product_key) 
    FROM Product p
)