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
