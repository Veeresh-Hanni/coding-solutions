# Biggest Single Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Table: `MyNumbers`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.

```

 

A  **single number**  is a number that appeared only once in the `MyNumbers` table.

Find the largest  **single number**. If there is no  **single number**, report `null`.

The result format is in the following example.

 

 **Example 1:** 

```
Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
Output: 
+-----+
| num |
+-----+
| 6   |
+-----+
Explanation: The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.

```

 **Example 2:** 

```
Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
Output: 
+------+
| num  |
+------+
| null |
+------+
Explanation: There are no single numbers in the input table so we return null.

```

## Solution

**Language:** SQL  
**Runtime:** 105 ms  
**Memory:** 0B  
**Submitted:** 2026-08-05T15:21:23.242Z  

```sql
# Write your MySQL query statement below

SELECT MAX(num) num FROM  myNUmbers 
GROUP BY num
HAVING COUNT(num) = 1;
```

---

[View on LeetCode](https://leetcode.com/problems/biggest-single-number/)