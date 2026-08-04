# Set .discard(), .remove() & .pop()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

__.remove(x)__<bR>  

This operation removes element $x$ from the set.  
If element $x$ does not exist, it raises a __`KeyError`__.<br>
The *.remove(x)* operation returns __`None`__.

**Example**
<pre>
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
</pre>
---
__.discard(x)__<br>  

This operation also removes element $x$ from the set.  
If element $x$ does not exist, it __does not__ raise a `KeyError`.<br>
The *.discard(x)* operation returns __`None`__.

**Example**
<pre>
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
</pre>
---
__.pop()__<br>  

This operation removes and return an arbitrary element from the set.  
If there are no elements to remove, it raises a __`KeyError`__.

**Example**
<pre>
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
</pre>  
---  
  
__Task__<br>  

You have a non-empty set $s$, and you have to execute $N$ commands given in $N$ lines.

The commands will be *pop, remove* and *discard*. 


**Input Format**

The first line contains integer $n$, the number of elements in the set $s$. <br>
The second line contains $n$ space separated elements of set $s$. All of the elements are non-negative integers, less than or equal to 9. <br>
The third line contains integer $N$, the number of commands.<br>
The next $N$ lines contains either *pop, remove* and/or *discard* commands followed by their associated value.

__Constraints__

$0 < n < 20 $  
$0 < N < 20$

**Output Format**

Print the sum of the elements of set $s$ on a single line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T08:00:39.074Z  

```py
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem)