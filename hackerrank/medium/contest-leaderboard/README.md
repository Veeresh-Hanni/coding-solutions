# Contest Leaderboard

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too! 

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the _hacker\_id_, _name_, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending _hacker\_id_. Exclude all hackers with a total score of $0$ from your result.


**Input Format**

The following tables contain contest data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker. <img src="https://s3.amazonaws.com/hr-challenge-images/19503/1458522826-a9ddd28469-ScreenShot2016-03-21at6.40.27AM.png"/>

- _Submissions:_ The _submission\_id_ is the id of the submission, _hacker\_id_ is the id of the hacker who made the submission, _challenge\_id_ is the id of the challenge for which the submission belongs to, and _score_ is the score of the submission. <img src="https://s3.amazonaws.com/hr-challenge-images/19503/1458523022-771511df90-ScreenShot2016-03-21at6.40.37AM.png"/>

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T14:28:55.566Z  

```sql
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/contest-leaderboard/problem)