#!/bin/python3

import os

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    freq = {}
    
    for a in arr:
        freq[a] = freq.get(a, 0) + 1
    
    
    max_id = 0
    max_val = float('-inf')
    for k, v in freq.items():

        if v > max_val or (v == max_val and k < max_id):
            max_id = k
            max_val = v
    return max_id
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
