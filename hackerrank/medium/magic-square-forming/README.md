# Cats and a Mouse

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

We define a [magic square](https://en.wikipedia.org/wiki/Magic_square) to be an $n \times n$ matrix of distinct positive integers from $1$ to $n^2$ where the sum of any row, column, or diagonal of length $n$ is always equal to the same number:  the *magic constant*. 

You will be given a $3 \times 3$ matrix $s$ of integers in the inclusive range $[1, 9]$. We can convert any digit $a$ to any other digit $b$ in the range $[1, 9]$ at cost of $|a - b|$.  Given $s$, convert it into a magic square at *minimal* cost. Print this cost on a new line.

**Note:** The resulting magic square must contain distinct integers in the inclusive range $[1, 9]$.


**Example**  

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]  

The matrix looks like this: 
```
5 3 4
1 5 8
6 4 2
```
We can convert it to the following magic square:
```
8 3 4
1 5 9
6 7 2
```
This took three replacements at a cost of $|5-8|+|8-9|+|4-7|=7$.

**Function Description**

Complete the *formingMagicSquare* function in the editor below.  

formingMagicSquare has the following parameter(s):  

- *int s[3][3]:* a $3 \times 3$ array of integers  

**Returns**  

- *int:*  the minimal total cost of converting the input square to a magic square 

**Input Format**

Each of the $3$ lines contains three space-separated integers of row $s[i]$.  

**Constraints**

- $s[i][j] \in [1, 9]$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T04:52:33.320Z  

```py
#!/bin/python3
import os

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # x = catA, y= catB, z = mouseC
    a_dis = abs(x - z)
    b_dis = abs(y - z)
    
    if a_dis == b_dis:
        return "Mouse C"
    elif a_dis < b_dis:
        return "Cat A"
    else:
        return "Cat B"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/magic-square-forming/problem)