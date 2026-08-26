#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_num = float('-inf')
    min_num = float('inf')
    
    max_count = 0
    min_count = 0
    
    for s in scores:
        if s > max_num:
            max_num = s
            max_count += 1
        if s < min_num :
            min_num = s
            min_count += 1
    
    return [max_count-1,min_count-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
