# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN id % 2 = 1 AND id = total_rows THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat, 
     (SELECT COUNT(*) AS total_rows FROM Seat) AS temp
ORDER BY id;