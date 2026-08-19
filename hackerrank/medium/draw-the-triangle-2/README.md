# Draw The Triangle 2

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_P(R)_ represents a pattern drawn by Julia in _R_ rows. The following pattern represents _P(5)_:

    * 
    * * 
    * * * 
    * * * * 
    * * * * *

Write a query to print the pattern _P(20)_.


**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T13:46:05.737Z  

```sql
/*
Enter your query here.
*/

WITH RECURSIVE numbers AS (

    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 20

)

SELECT REPEAT('* ', n)
FROM numbers;

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/draw-the-triangle-2/problem)