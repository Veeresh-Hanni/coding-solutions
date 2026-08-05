# Write your MySQL query statement below

SELECT MAX(num) num FROM  myNUmbers 
GROUP BY num
HAVING COUNT(num) = 1;