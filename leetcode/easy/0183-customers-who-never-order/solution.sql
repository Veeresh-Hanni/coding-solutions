# Write your MySQL query statement below
-- SELECT name as Customers From Customers WHERE id NOT in 
-- (SELECT c.id as id FROM Customers c 
-- JOIN Orders o on c.id = o.customerId);

SELECT c.name AS Customers FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL