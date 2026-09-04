# Divisible Sum Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers and a positive integer $k$, determine the number of $(i, j)$ pairs where $i \lt j$ and $ar[i]$ + $ar[j]$ is divisible by $k$.  

**Example**  

$ar = [1, 2, 3, 4, 5, 6]$   
$k = 5$   

Three pairs meet the criteria:  $[1, 4], [2, 3],$ and $[4, 6]$.  

**Function Description**

Complete the *divisibleSumPairs* function in the editor below.   

divisibleSumPairs has the following parameter(s):  

- *int n:* the length of array $ar$  
- *int ar[n]:* an array of integers  
- *int k:* the integer divisor   

**Returns**  
-	*int:* the number of pairs  

**Input Format**

The first line contains $2$ space-separated integers, $n$ and $k$.	
The second line contains $n$ space-separated integers, each a value of $arr[i]$.  



**Constraints**

* $2 \leq n \leq 100$
* $1 \leq k \leq 100$
* $1 \leq ar[i] \leq 100$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T14:19:41.337Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    
    count_pairs = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0 and i < j:
                count_pairs += 1
    return count_pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/divisible-sum-pairs/problem)