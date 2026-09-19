# String Difference

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings, str1, and str2, where str1 contains exactly one character more than str2, find the indices of the characters in str1 that can be removed to make str1 equal to str2. Return the array of indices in increasing order. If it is not possible, return the array [-1]. 

 **Note:**  Use 0-based indexing.

 **Example** 

str1 = "abdgggda" str2 = "abdggda"

Any "g" character at positions 3, 4, or 5 can be deleted to obtain str2. Return [3, 4, 5].

 **Input Format** 

 **Function Description** 

Complete the function  *getRemovableIndices*  in the editor below.

 *getRemovableIndices*  has the following parameters:

- string str1: the string to modify
- string str2: the target string

 **Constraints** 

 **Constraints** 

- 2 ≤ |str1| ≤ 2 * 10^5
- 1 ≤ |str2| ≤ 2 * 10^5
- |str1| = |str2| + 1 
- str1 and str2 only contain lowercase English letters.

 **Output Format** 

 **Output Format** 

     int[]: the indices of characters that can be removed from str1 in ascending order, or [-1] if it is not possible to match str2

 **Sample Input 0** 

```
aabbb
aabb

```

 **Sample Output 0** 

```
2
3
4

```

 **Explanation 0** 

From str1, a character at indices 2, 3, or 4 can be removed to make it equal to str2.

 **Sample Input 1** 

```
mmgghh
mfggh

```

 **Sample Output 1** 

```
-1

```

 **Explanation 1** 

There is no way to make str1 equal to str2 by removing any 1 character.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T06:42:45.200Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

def getRemovableIndices(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    
    if n1 != n2 + 1:
        return [-1]
        
    # Find the longest common prefix length from the left
    left = 0
    while left < n2 and str1[left] == str2[left]:
        left += 1
        
    # Find the longest common suffix length from the right
    right = 0
    while right < n2 and str1[n1 - 1 - right] == str2[n2 - 1 - right]:
        right += 1
        
    # If prefix and suffix don't cover enough characters, it's impossible
    if left + right < n2:
        return [-1]
        
    # The valid indices to remove lie in the range [n2 - right, left]
    start = n2 - right
    end = left
    
    # Since all characters in this overlapping mismatch region are identical,
    # every index in this range is a valid removable index.
    return list(range(start, end + 1))
     
if __name__ == '__main__':
    str1 = input()
    str2 = input()

    result = getRemovableIndices(str1, str2)

    print('\n'.join(map(str, result)))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/string-difference-1-4/problem)