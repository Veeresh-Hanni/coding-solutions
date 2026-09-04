# Divisible Sum Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type.  If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

**Example**    
$arr = [1,1,2,2,3]$   

There are two each of types $1$ and $2$, and one sighting of type $3$.  Pick the lower of the two types seen twice: type $1$.  

**Function Description**

Complete the *migratoryBirds* function in the editor below.    

migratoryBirds has the following parameter(s):  

- *int arr[n]*: the types of birds sighted   

**Returns**   

- *int:* the lowest type id of the most frequently sighted birds   

**Input Format**

The first line contains an integer, $n$, the size of $arr$.		
The second line describes $arr$ as $n$ space-separated integers, each a type number of the bird sighted.

**Constraints**

+ $5 \le n \le 2 \times 10^5$
- It is guaranteed that each type is $1$, $2$, $3$, $4$, or $5$.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T14:20:00.346Z  

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

[View on HackerRank](https://www.hackerrank.com/challenges/migratory-birds/problem)