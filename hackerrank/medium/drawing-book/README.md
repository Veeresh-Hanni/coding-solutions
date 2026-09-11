# Bill Division

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time.  When they open the book, page $1$ is always on the right side:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481920803-d2b54f38f0-book.png)

When they flip page $1$, they see pages $2$ and $3$.  Each page except the last page will always be printed on both sides.  The last page may only be printed on the front, given the length of the book.  If the book is $n$ pages long, and a student wants to turn to page $p$, what is the minimum number of pages to turn?  They can start at the beginning or the end of the book. 

Given $n$ and $p$, find and print the minimum number of pages that must be turned in order to arrive at page $p$. 

**Example**  

$n = 5$  
$p = 3$  

![Untitled Diagram(4).png](https://s3.amazonaws.com/hr-challenge-images/22564/1467398281-32b69f6fa9-UntitledDiagram4.png)

Using the diagram above, if the student wants to get to page $3$, they open the book to page $1$, flip $1$ page and they are on the correct page.  If they open the book to the last page, page $5$, they turn $1$ page and are at the correct page.  Return $1$. 

**Function Description**  

Complete the *pageCount* function in the editor below.  

pageCount has the following parameter(s):  

- *int n*: the number of pages in the book   
- *int p*: the page number to turn to  

**Returns**  

- *int:* the minimum number of pages to turn

**Input Format**

The first line contains an integer $n$, the number of pages in the book.	
The second line contains an integer, $p$, the page to turn to.

**Constraints**

* $1 \le n \le 10^5$
* $1 \le p \le n$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T14:03:17.911Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    anna_amount = 0
    
    for i in range(len(bill)):
        if i != k:
            anna_amount += bill[i]
    
    if  (anna_amount // 2)  == b:
        print("Bon Appetit")
    else:
        print(b - (anna_amount // 2))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/drawing-book/problem)