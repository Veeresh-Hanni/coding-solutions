#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    days_in_8m_year = 243

    if year == 1918:
        return f"26.09.{year}"

    if year < 1918:
        # Julian calendar
        if year % 4 == 0:
            days_in_8m_year += 1
    else:
        # Gregorian calendar
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days_in_8m_year += 1

    return f"{256 - days_in_8m_year:02d}.09.{year}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
