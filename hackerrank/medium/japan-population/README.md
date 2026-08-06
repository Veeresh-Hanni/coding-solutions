# Japan Population

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Query the sum of the populations for all Japanese cities in **CITY**. The *COUNTRYCODE* for Japan is **JPN**.


**Input Format**

The **CITY** table is described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T07:31:37.823Z  

```sql
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN';

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/japan-population/problem)