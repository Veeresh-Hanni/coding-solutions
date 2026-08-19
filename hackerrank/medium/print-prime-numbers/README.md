# Draw The Triangle 2

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a query to print all *prime numbers* less than or equal to $1000$. Print your result on a single line, and use the ampersand ($\&$) character as your separator (instead of a space).


For example, the output for all prime numbers $\leq 10$ would be:

	2&3&5&7

**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T13:46:17.551Z  

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

[View on HackerRank](https://www.hackerrank.com/challenges/print-prime-numbers/problem)