/*
Enter your query here.
*/

SELECT h.hacker_id, h.name, count(c.challenge_id) as challenges_created
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING challenges_created = (
    SELECT MAX(challenge_count)
    FROM (
        SELECT COUNT(*) AS challenge_count
        FROM Challenges
        GROUP BY hacker_id
    ) x
)
OR challenges_created IN (
    SELECT challenge_count
    FROM (
        SELECT COUNT(*) AS challenge_count
        FROM Challenges
        GROUP BY hacker_id
    ) y
    GROUP BY challenge_count
    HAVING COUNT(*) = 1
)
ORDER BY challenges_created DESC, h.hacker_id;
