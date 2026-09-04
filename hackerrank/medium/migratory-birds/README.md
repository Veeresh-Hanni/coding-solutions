# Migratory Birds

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type.  If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

**Example**    
$arr = [1,1,2,2,3]$   

There are two each of types $1$ and $2$, and one sighting of type $3$.  Pick the lower of the two types seen twice: type $1$.  

**Function Description**

Complete the *migratoryBirds* function in the editor below.    

migratoryBirds has the following parameter(s):  

- *int arr[n]*: the types of birds sighted   

**Returns**   

- *int:* the lowest type id of the most frequently sighted birds   

**Input Format**

The first line contains an integer, $n$, the size of $arr$.		
The second line describes $arr$ as $n$ space-separated integers, each a type number of the bird sighted.

**Constraints**

+ $5 \le n \le 2 \times 10^5$
- It is guaranteed that each type is $1$, $2$, $3$, $4$, or $5$.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T14:41:21.452Z  

```py
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
    # freq = {}
    
    # for a in arr:
    #     freq[a] = freq.get(a, 0) + 1
    
    
    # max_id = 0
    # max_val = float('-inf')
    # for k, v in freq.items():

    #     if v > max_val or (v == max_val and k < max_id):
    #         max_id = k
    #         max_val = v
    # return max_id
    
    freq = [0] * 6

    for bird in arr:
        freq[bird] += 1

    max_count = 0
    answer = 0

    for bird in range(1, 6):
        if freq[bird] > max_count:
            max_count = freq[bird]
            answer = bird

    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/migratory-birds/problem)