# Contest Leaderboard

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Julia conducted a $15$ days of learning SQL contest. The start date of the contest was _March 01, 2016_ and the end date was _March 15, 2016_. 

Write a query to print total number of unique hackers who made at least $1$ submission each day (starting on the first day of the contest), and find the _hacker\_id_ and _name_ of the hacker who made maximum number of submissions each day. If more than one such hacker has a maximum number of submissions, print the lowest *hacker\_id*. The query should print this information for each day of the contest, sorted by the date.

----

**Input Format**

The following tables hold contest data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker.<img src="https://s3.amazonaws.com/hr-challenge-images/19597/1458511164-12adec3b8b-ScreenShot2016-03-21at3.26.47AM.png"/>

- _Submissions:_ The _submission\_date_ is the date of the submission, _submission\_id_ is the id of the submission, _hacker\_id_ is the id of the hacker who made the submission, and _score_ is the score of the submission. <img src="https://s3.amazonaws.com/hr-challenge-images/19597/1458511251-0b534030b9-ScreenShot2016-03-21at3.26.56AM.png"/>

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T14:29:25.385Z  

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

[View on HackerRank](https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem)