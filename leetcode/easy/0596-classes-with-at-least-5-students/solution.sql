# Write your MySQL query statement below


SELECT class FROM (
    SELECT student, class FROM Courses
    group by class 
    having count(class) >= 5
) t
