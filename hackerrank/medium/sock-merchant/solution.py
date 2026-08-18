#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    # pairs = 0
    
    # for right in range(n):
    #     if ar[right - 1] == ar[right]:
    #         pairs += 1
    # return pairs
    
    pairs = {}
    count = 0
    for el in ar:
        pairs[el] = pairs.get(el, 0) + 1
    
    for k, v in pairs.items():
        
        if v % 2 == 0 and v > 2:
            count += 2
        else:
            count = count + v // 2
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
