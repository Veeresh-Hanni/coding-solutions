# Set Mutations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

We have seen the applications of *union, intersection, difference* and *symmetric difference* operations, but these operations do not make any changes or mutations to the set.  

**We can use the following operations to create mutations to a set:**

__.update()__ or __`|=`__ <br>
Update the set by adding elements from an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
```

__.intersection_update()__ or __`&=`__<br>
Update the set by keeping only the elements found in it and an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
```

__.difference_update()__ or __`-=`__<br>
Update the set by removing elements found in an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
```

__.symmetric_difference_update()__ or __`^=`__<br>
Update the set by only keeping the elements found in either set, but not in both.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
```

---

__TASK__<br>
You are given a set $A$ and $N$ number of other sets. These $N$ number of sets have to perform some specific mutation operations on set $A$.

Your task is to execute those operations and print the sum of elements from set $A$.


**Input Format**

The first line contains the number of elements in set $A$.<br>
The second line contains the space separated list of elements in set $A$.<bR>
The third line contains integer $N$, the number of other sets.<br>
The next $2*N$ lines are divided into $N$ parts containing two lines each.<br>
The first line of each part contains the space separated entries of the _operation name_ and the _length of the other set_.<br>
The second line of each part contains space separated list of elements in the other set.<bR>

$0 <$ *len(set(__A__))* $< 1000$ <br>
$0 <$ *len(otherSets)* $< 100$ <br>
$0 < N < 100$

**Output Format**

Output the sum of elements in set $A$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T08:19:05.306Z  

```py
n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    cmd, _ = input().split()

    other = set(map(int, input().split()))

    if cmd == "intersection_update":
        A.intersection_update(other)

    elif cmd == "update":
        A.update(other)

    elif cmd == "symmetric_difference_update":
        A.symmetric_difference_update(other)

    elif cmd == "difference_update":
        A.difference_update(other)

print(sum(A))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-set-mutations/problem)