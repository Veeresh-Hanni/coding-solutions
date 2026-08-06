# Weather Observation Station 2

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Query the following two values from the **STATION** table: 

1. The sum of all values in *LAT\_N* rounded to a scale of $2$ decimal places.
2. The sum of all values in *LONG\_W* rounded to a scale of $2$ decimal places.

**Input Format**

The **STATION** table is described as follows:

![Station.jpg](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude.

**Constraints**

 

**Output Format**

Your results must be in the form:

	lat lon
    
where $lat$ is the sum of all values in *LAT\_N* and $lon$ is the sum of all values in *LONG\_W*. Both results must be rounded to a scale of $2$ decimal places.

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T07:49:49.325Z  

```sql
/*
Enter your query here.
*/

SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2) FROM STATION;

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-2/problem)