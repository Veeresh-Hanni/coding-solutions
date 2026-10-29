# Write your MySQL query statement below
-- SELECT department, employee, hsalary
-- FROM (
--     SELECT d.name as department , e.name as employee, 
--             MAX(e.salary) OVER(
--                 PARTITION BY d.name
--             )as hsalary

--     FROM Employee e

--     JOIN department d On e.departmentId = d.id) t

-- WHERE e.salary = hsalary;

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