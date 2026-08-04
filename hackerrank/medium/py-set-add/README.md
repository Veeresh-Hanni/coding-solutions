# Set .add()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

If we want to add a single element to an existing set, we can use the *.add()* operation. <br>
It adds the element to the set and returns '__```None```__'.

__Example__

    >>> s = set('HackerRank')
    >>> s.add('H')
    >>> print s
    set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
    >>> print s.add('HackerRank')
    None
    >>> print s
    set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
  
 <BR> 
__Task__  

Apply your knowledge of the *.add()* operation to help your friend Rupal.<br><br>
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of $N$ country stamps.<br><br>
Find the total number of distinct country stamps.




**Input Format**

The first line contains an integer $N$, the total number of country stamps.<br>
The next $N$ lines contains the name of the country where the stamp is from. <br>  

__Constraints__  

$0 < N < 1000$

**Constraints**

 

**Output Format**

Output the total number of distinct country stamps on a single line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T07:48:31.701Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

stamps = set()

for _ in range(N):
    stamps.add(input())

print(len(stamps))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-set-add/problem)