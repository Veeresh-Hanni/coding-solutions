#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    
    # Approach 1 Brite force
    # count = 0
    # n = len(s)
    
    # for idx in range(n - m + 1):
    #     if sum(s[idx:idx+m]) == d:
    #         count += 1
    # return count
    
    # Approach 2 sliding window
    count = 0
    window_sum = sum(s[:m])

    if window_sum == d:
        count += 1

    for i in range(m, len(s)):
        window_sum += s[i]       # add right
        window_sum -= s[i - m]  # remove left

        if window_sum == d:
            count += 1

    return count    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
