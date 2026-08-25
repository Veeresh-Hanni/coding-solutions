/*
Enter your query here.
*/
SELECT
    h.hacker_id,
    h.name,
    x.total_score
FROM Hackers h
JOIN (
    SELECT
        hacker_id,
        SUM(max_score) AS total_score
    FROM (
        SELECT
            hacker_id,
            challenge_id,
            MAX(score) AS max_score
        FROM Submissions
        GROUP BY hacker_id, challenge_id
    ) s
    GROUP BY hacker_id
) x
ON h.hacker_id = x.hacker_id
WHERE x.total_score > 0
ORDER BY x.total_score DESC, h.hacker_id ASC;
