# Summing the N series

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is a sequence whose $n^{\text{th}}$ term is  
$$T_n = n^2 - (n-1)^2$$  

Evaluate the series  
$$S_n = T_1 + T_2 + T_3 + \cdots + T_n$$  
Find $S_n \bmod (10^9+7)$.  

**Example**  

$n = 3$  

The series is $1^2-0^2 + 2^2-1^2 + 3^2-2^2 = 1 + 3 + 5 = 9$.  

**Function Description**  

Complete the *summingSeries* function in the editor below.  

*summingSeries* has the following parameter(s):  

- *int n:* the inclusive limit of the range to sum  

**Returns**  

- *int:* the sum of the sequence, modulo $(10^9+7)$  



**Input Format**

The first line of input contains $t$, the number of test cases.  
Each test case consists of one line containing a single integer $n$.  

**Constraints**

+ $1 \le t \le 10$  
+ $1 \le n \le 10^{16}$  

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T14:41:51.818Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def summingSeries(n):
    # Write your code here
    
    # result = 0
    
    # if n == 1:
    #     return 1
    # elif n == 0:
    #     return 0
     
    # while n:
    #     result += (n**2 - ((n - 1) ** 2))
    #     n -= 1
    # return result
    MOD = 10**9 + 7
    return (n * n) % MOD
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/summing-the-n-series/problem)