# Write your MySQL query statement below


SELECT Department, Employee, hsalary as Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary,
        MAX(e.salary) OVER (
            PARTITION BY d.name
        ) AS hsalary
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
) t
WHERE salary = hsalary;