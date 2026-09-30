# max-unique-substring-length-in-session

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T05:01:05.055Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    # Write your code here
    if not sessionString or len(sessionString) == 1:
        return 0
    
    char_index = {}
    left = 0
    max_len = 0
    
    for right in range(len(sessionString)):
        current_char = sessionString[right]
        
        # Session separator (e.g., space ' ') bandre window na reset madi
        if current_char == ' ':
            left = right + 1
            char_index.clear() # Previous session characters na clear madi
            continue
            
        # Character duplicate idre, left pointer na update madi
        if current_char in char_index and char_index[current_char] >= left:
            left = char_index[current_char] + 1
            
        # Character index na store/update madi
        char_index[current_char] = right
        
        # Max length calculate madi
        max_len = max(max_len, right - left + 1)
        
    return max_len

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/max-unique-substring-length-in-session/problem)