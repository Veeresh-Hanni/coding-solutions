# Weather Observation Station 17

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider $P_1(a, b)$ and $P_2(c, d)$ to be two points on a *2D* plane.

- $a$ happens to equal the minimum value in *Northern Latitude* (*LAT\_N* in **STATION**).
- $b$ happens to equal the minimum value in *Western Longitude* (*LONG\_W* in **STATION**).
- $c$ happens to equal the maximum value in *Northern Latitude* (*LAT\_N* in **STATION**).
- $d$ happens to equal the maximum value in *Western Longitude* (*LONG\_W* in **STATION**).

Query the [Manhattan Distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html)  between points $P_1$ and $P_2$ and round it to a scale of $4$ decimal places.


**Input Format**

The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude. 

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T08:16:00.994Z  

```sql
/*
Enter your query here.
*/

SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (
    SELECT MIN(LAT_N)
    FROM STATION
    WHERE LAT_N > 38.7780
);

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-18/problem)