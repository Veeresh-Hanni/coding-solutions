#!/bin/python3
import os

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # x = catA, y= catB, z = mouseC
    a_dis = abs(x - z)
    b_dis = abs(y - z)
    
    if a_dis == b_dis:
        return "Mouse C"
    elif a_dis < b_dis:
        return "Cat A"
    else:
        return "Cat B"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
