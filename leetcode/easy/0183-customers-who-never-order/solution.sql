# Write your MySQL query statement below
-- SELECT name as Customers From Customers WHERE id NOT in 
-- (SELECT c.id as id FROM Customers c 
-- JOIN Orders o on c.id = o.customerId);

select c.name as Customers from Customers c
left join Orders o
on c.id = o.customerId
where o.customerId is null