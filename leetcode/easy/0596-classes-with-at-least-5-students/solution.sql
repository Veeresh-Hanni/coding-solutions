# Write your MySQL query statement below


SELECT class FROM (
    SELECT student, class FROM Courses
    group by student 
    order by COUNT(class) DESC
    limit 1
) t
