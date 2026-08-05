# Write your MySQL query statement below

SELECT MAX(num) as num FROM 
    (SELECT num FROM myNUmbers 
    GROUP BY num
    HAVING COUNT(num) = 1) t