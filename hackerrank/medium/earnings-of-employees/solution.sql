/*
Enter your query here.
*/

SELECT
    salary * months AS earnings,
    COUNT(*) AS employee_count
FROM Employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;
