#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def getRemovableIndices(str1, str2):

    freq1 = {}
    freq2 = {}

    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1

    removal_char = None

    for char in freq1:
        if freq2[char] == 1:
            return [-1]
        
        elif freq1[char] == freq2.get(char, 0) + 1:
            removal_char = char
            break

    if removal_char is None:
        return [-1]

    result = []

    for idx in range(len(str1)):
        if str1[idx] == removal_char:
            result.append(idx)

    return result

if __name__ == '__main__':
    str1 = input()

    str2 = input()

    result = getRemovableIndices(str1, str2)

    print('\n'.join(map(str, result)))
