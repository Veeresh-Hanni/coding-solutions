# Triangle Judgement

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Table: `Triangle`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

```

 

Report for every three line segments whether they can form a triangle.

Return the result table in  **any order**.

The result format is in the following example.

 

 **Example 1:** 

```
Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

```

## Solution

**Language:** SQL  
**Runtime:** 348 ms (beats 19.40%)  
**Memory:** 0B (beats 100.00%)  
**Submitted:** 2026-08-05T15:14:22.390Z  

```sql
# Write your MySQL query statement below

-- SELECT *,
--     CASE 
--         WHEN x + y > z AND x + z > y AND y + z > x THEN "Yes" 
--         ELSE "No"
--     END as triangle
-- FROM Triangle;

SELECT 
    *, 
    IF(x + y > z AND y + z > x AND  x + z > y, "Yes", "No") AS triangle 
FROM 
    Triangle;
```

---

[View on LeetCode](https://leetcode.com/problems/triangle-judgement/)