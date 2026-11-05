# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id  -- Last row (if odd) stays same
        WHEN id % 2 = 1 THEN id + 1                                  -- Odd IDs move down
        ELSE id - 1                                                  -- Even IDs move up
    END AS id,
    student
FROM Seat
ORDER BY id;