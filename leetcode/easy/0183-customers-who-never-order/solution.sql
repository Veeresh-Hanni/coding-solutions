# Write your MySQL query statement below
SELECT name as Customers From Customers WHERE id NOT in 
(SELECT c.id as id FROM Customers c 
JOIN Orders o on c.id = o.customerId);