# No Idea!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is an array of $n$ integers. There are also $2$ **disjoint sets**, $A$ and $B$, each containing $m$ integers. You like all the integers in set $A$ and dislike all the integers in set $B$. Your initial happiness is $0$. For each $i$ integer in the array, if $i\in A$, you add $1$ to your happiness. If $i\in B$, you add $-1$ to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.  

**Note:** Since $A$ and $B$ are sets, they have no repeated elements. However, the array might contain duplicate elements.  

**Constraints**  
$1\le n\le 10^5$  
$1\le m\le 10^5$  
$1\le Any\ integer\ in\ the\ input\le 10^9$  

**Input Format**

The first line contains integers $n$ and $m$ separated by a space.  
The second line contains $n$ integers, the elements of the array.  
The third and fourth lines contain $m$ integers, $A$ and $B$, respectively.

**Output Format**

Output a single integer, your total happiness.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T07:35:20.367Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT


n, m = map(int, input().split())

arr = list(map(int, input().split()))

a = set(map(int, input().split()))

b = set(map(int, input().split()))

# a_happines = 0
# b_happiness = 0

# for n in arr:
#     if n in a:
#         a_happines += 1
#     elif n in b:
#         b_happiness += 1

# print(a_happines - b_happiness)
happiness = 0

for num in arr:
    if num in a:
        happiness += 1
    elif num in b:
        happiness -= 1

print(happiness)
# print(n)
# print(m)
# print(arr)
# print(a)
# print(b)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/no-idea/problem)