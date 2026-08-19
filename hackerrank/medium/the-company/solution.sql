/*
Enter your query here.
*/

-- SELECT DISTINCT c.company_code, c.founder, 
--     COUNT(DISTINCT l.Lead_Manager_code),
--     COUNT(DISTINCT s.Senior_Manager_code),
--     COUNT(DISTINCT m.Manager_code),
--     COUNT(DISTINCT e.employee_code)
-- FROM Company c 

-- JOIN Lead_Manager l ON c.company_code = l.company_code

-- JOIN Senior_MAnager s ON l.Lead_Manager_code = s.Lead_Manager_code

-- JOIN Manager m ON s.Senior_MAnager_code = m.Senior_MAnager_code

-- JOIN Employee e ON m.Manager_code = e.Manager_code

-- GROUP BY c.company_code, c.founder

-- ORDER BY LENGTH(c.company_code) ASC, c.company_code ASC ;

SELECT 
    c.company_code,
    c.founder,
    COUNT(DISTINCT l.Lead_Manager_code) AS lead_manager_count,
    COUNT(DISTINCT s.Senior_Manager_code) AS senior_manager_count,
    COUNT(DISTINCT m.Manager_code) AS manager_count,
    COUNT(DISTINCT e.employee_code) AS employee_count
FROM Company c
JOIN Lead_Manager l
    ON c.company_code = l.company_code
JOIN Senior_Manager s
    ON l.Lead_Manager_code = s.Lead_Manager_code
JOIN Manager m
    ON s.Senior_Manager_code = m.Senior_Manager_code
JOIN Employee e
    ON m.Manager_code = e.Manager_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code ;
