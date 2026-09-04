# Migratory Birds

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Marie invented a [Time Machine](https://en.wikipedia.org/wiki/Time_machine) and wants to test it by time-traveling to visit Russia on the [Day of the Programmer](https://en.wikipedia.org/wiki/Day_of_the_Programmer) (the 256th day of the year) during a year in the inclusive range from 1700 to 2700. 

From 1700 to 1917, Russia's official calendar was the [Julian calendar](https://en.wikipedia.org/wiki/Julian_calendar); since 1919 they used the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a *leap year*, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

- Divisible by 400.
- Divisible by 4 and *not* divisible by 100.

Given a year, $y$, find the date of the 256th day of that year *according to the official Russian calendar during that year*. Then print it in the format `dd.mm.yyyy`, where `dd` is the two-digit day, `mm` is the two-digit month, and `yyyy` is $y$.

For example, the given $year$ = 1984.  1984 is divisible by 4, so it is a leap year.  The 256th day of a leap year after 1918 is September 12, so the answer is $\texttt{12.09.1984}$.  

**Function Description**  

Complete the *dayOfProgrammer* function in the editor below.  It should return a string representing the date of the 256th day of the year given.  

dayOfProgrammer has the following parameter(s):  

- *year*: an integer  

**Input Format**

A single integer denoting year $y$.

**Constraints**

- 1700 \le y \le 2700

**Output Format**

Print the full date of *Day of the Programmer* during year $y$ in the format `dd.mm.yyyy`, where `dd` is the two-digit day, `mm` is the two-digit month, and `yyyy` is $y$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T14:42:08.829Z  

```py
#!/bin/python3

import os

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    # freq = {}
    
    # for a in arr:
    #     freq[a] = freq.get(a, 0) + 1
    
    
    # max_id = 0
    # max_val = float('-inf')
    # for k, v in freq.items():

    #     if v > max_val or (v == max_val and k < max_id):
    #         max_id = k
    #         max_val = v
    # return max_id
    
    freq = [0] * 6

    for bird in arr:
        freq[bird] += 1

    max_count = 0
    answer = 0

    for bird in range(1, 6):
        if freq[bird] > max_count:
            max_count = freq[bird]
            answer = bird

    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/day-of-the-programmer/problem)