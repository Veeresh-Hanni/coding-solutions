# Write your MySQL query statement below



SELECT class FROM Courses
group by class 
having count(class) >= 5

