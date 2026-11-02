# Write your MySQL query statement below

SELECT Department, Employee, Salary
FROM 
    (SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
            DENSE_RANK() OVER(PARTITION BY d.name

            ORDER by e.salary DESC) as drk

    FROM Employee e JOIN Department d on e.departmentId = d.id) as x

WHERE drk <= 3;