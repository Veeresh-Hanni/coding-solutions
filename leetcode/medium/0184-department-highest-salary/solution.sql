# Write your MySQL query statement below


-- SELECT Department, Employee, hsalary as Salary
-- FROM (
--     SELECT 
--         d.name AS Department,
--         e.name AS Employee,
--         e.salary,
--         MAX(e.salary) OVER (
--             PARTITION BY d.name
--         ) AS hsalary
--     FROM Employee e
--     JOIN Department d
--         ON e.departmentId = d.id
-- ) t
-- WHERE salary = hsalary;


SELECT d.name as Department, 
       e.name as Employee,
       e.salary as Salary
    FROM
    (
        SELECT 
        e.*,
        RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as rnk
        FROM employee e 
    ) e 
    JOIN department d ON e.departmentId = d.id
    WHERE rnk = 1