# Occupations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

[Pivot](https://en.wikipedia.org/wiki/Pivot_table) the *Occupation* column in **OCCUPATIONS** so that each *Name* is sorted alphabetically and displayed underneath its corresponding *Occupation*. The output should consist of four columns (*Doctor*, *Professor*, *Singer*, and *Actor*) in that specific order, with their respective names listed alphabetically under each column.

**Note:** Print **NULL** when there are no more names corresponding to an occupation.


**Input Format**

The **OCCUPATIONS** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12889/1443816414-2a465532e7-1.png" />

*Occupation* will only contain one of the following values: **Doctor**, **Professor**, **Singer** or **Actor**.

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T06:42:11.411Z  

```sql
/*
Enter your query here.
*/

SELECT 
    MAX(CASE WHEN occupation='Doctor' THEN name END),
    MAX(CASE WHEN occupation='Professor' THEN name END),
    MAX(CASE WHEN occupation='Singer' THEN name END),
    MAX(CASE WHEN occupation='Actor' THEN name END)
FROM 
    (SELECT
        name,
        occupation,
        ROW_NUMBER() OVER(
            PARTITION BY occupation
            ORDER BY name
        ) AS rn
    FROM Occupations) t 
GROUP BY rn;

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/occupations/problem)