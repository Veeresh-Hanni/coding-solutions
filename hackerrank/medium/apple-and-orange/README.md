# Apple and Orange

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.  

In the diagram below: 

- The red region denotes the house, where $s$ is the start point, and $t$ is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right. 
- Assume the trees are located on a single point, where the apple tree is at point $a$, and the orange tree is at point $b$.
- When a fruit falls from its tree, it lands $d$ units of distance from its tree of origin along the $x$-axis. *A negative value of $d$ means the fruit fell $d$ units to the tree's left, and a positive value of $d$ means it falls $d$ units to the tree's right. *

![Apple and orange(2).png](https://s3.amazonaws.com/hr-challenge-images/25220/1474218925-f2a791d52c-Appleandorange2.png)

Given the value of $d$ for $m$ apples and $n$ oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range $[s, t]$)?

For example, Sam's house is between $s = 7$ and $t = 10$.  The apple tree is located at $a = 4$ and the orange at $b = 12$.  There are $m = 3$ apples and $n = 3$ oranges.  Apples are thrown $apples = [2, 3, -4]$ units distance from $a$, and $oranges = [3, -2, -4]$ units distance.  Adding each apple distance to the position of the tree, they land at $[4 + 2, 4 + 3, 4 + -4] = [6, 7, 0]$.  Oranges land at $[12 + 3, 12 + -2, 12 + -4] = [15, 10, 8]$.  One apple and two oranges land in the inclusive range $7-10$ so we print 

    1
    2

**Function Description**  

Complete the *countApplesAndOranges* function in the editor below.  It should print the number of apples and oranges that land on Sam's house, each on a separate line.  

countApplesAndOranges has the following parameter(s):  

- *s*: integer, starting point of Sam's house location.       
- *t*: integer, ending location of Sam's house location.     
- *a*: integer, location of the Apple tree.      
- *b*: integer, location of the Orange tree.         
- *apples*: integer array, distances at which each apple falls from the tree.      
- *oranges*: integer array, distances at which each orange falls from the tree.  

**Input Format**

The first line contains two space-separated integers denoting the respective values of $s$ and $t$.		
The second line contains two space-separated integers denoting the respective values of $a$ and $b$.		
The third line contains two space-separated integers denoting the respective values of $m$ and $n$.			
The fourth line contains $m$ space-separated integers denoting the respective distances that each apple falls from point $a$.		
The fifth line contains $n$ space-separated integers denoting the respective distances that each orange falls from point $b$.

**Constraints**

* $1 \le s, t, a, b, m, n \le 10^{5} $
* $-10^{5} \le d \le 10^{5} $
* $ a < s < t < b $

**Output Format**

Print two integers on two different lines:

1. The first integer:  the number of apples that fall on Sam's house.
2. The second integer:  the number of oranges that fall on Sam's house.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T13:37:44.063Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    orange_count = 0
    
    for ap in apples:
        if (a + ap) >= s and (a + ap) <= t:
            apple_count += 1
    
    for ora in oranges:
        if (ora + b) >= s and (b + ora) <= t:
            orange_count += 1
    
    print(apple_count) 
    print(orange_count)
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/apple-and-orange/problem)