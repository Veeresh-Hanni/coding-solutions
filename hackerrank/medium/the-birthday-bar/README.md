# Breaking the Records

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it. 

Lily decides to share a contiguous segment of the bar selected such that: 

- The length of the segment matches Ron's birth month, and,
- The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.

**Example**   
$s = [2, 2, 1, 3, 2]$    
$d = 4$   
$m = 2$   

Lily wants to find segments summing to Ron's birth day, $d = 4$ with a length equalling his birth month, $m = 2$.  In this case, there are two segments meeting her criteria: $[2, 2]$ and $[1,3]$.

**Function Description**

Complete the *birthday* function in the editor below.    

birthday has the following parameter(s):  

- *int s[n]:* the numbers on each of the squares of chocolate  
- *int d:* Ron's birth day  
- *int m:* Ron's birth month  

**Returns**   

- *int:* the number of ways the bar can be divided  



**Input Format**

The first line contains an integer $n$, the number of squares in the chocolate bar.  	
The second line contains $n$ space-separated integers $s[i]$, the numbers on the chocolate squares where $0 \le i \lt n$.  
The third line contains two space-separated integers, $d$ and $m$, Ron's birth day and his birth month.

**Constraints**

* ${1} \leq {n} \leq 100$  
* ${1}\leq {s[i]}\leq {5}$, where (${0}\leq {i} \lt {n}$)     
* ${1} \leq {d} \leq {31}$  
* ${1} \leq {m} \leq {12}$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T05:28:00.993Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_num = float('-inf')
    min_num = float('inf')
    
    max_count = 0
    min_count = 0
    
    for s in scores:
        if s > max_num:
            max_num = s
            max_count += 1
        if s < min_num :
            min_num = s
            min_count += 1
    
    return [max_count-1,min_count-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/the-birthday-bar/problem)