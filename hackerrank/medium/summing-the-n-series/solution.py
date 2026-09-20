#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def summingSeries(n):
    # Write your code here
    
    # result = 0
    
    # if n == 1:
    #     return 1
    # elif n == 0:
    #     return 0
     
    # while n:
    #     result += (n**2 - ((n - 1) ** 2))
    #     n -= 1
    # return result
    MOD = 10**9 + 7
    return (n * n) % MOD
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
