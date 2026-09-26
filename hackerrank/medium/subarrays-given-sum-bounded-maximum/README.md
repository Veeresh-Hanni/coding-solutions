# subarrays-given-sum-bounded-maximum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T07:03:15.823Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. LONG_INTEGER k
#  3. LONG_INTEGER M
#

def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    count = 0

    prefix_sum = 0

    # prefix sum 0 exists before the array starts
    frequency = {0: 1}

    for num in nums:

        # num cannot belong to any valid subarray
        if num > M:
            prefix_sum = 0
            frequency = {0: 1}
            continue

        prefix_sum += num

        # Need an earlier prefix_sum = current - k
        count += frequency.get(prefix_sum - k, 0)

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    k = int(input().strip())

    M = int(input().strip())

    result = countSubarraysWithSumAndMaxAtMost(nums, k, M)

    print(result)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/subarrays-given-sum-bounded-maximum/problem)