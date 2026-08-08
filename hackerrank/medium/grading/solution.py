#!/bin/python3

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
import os
def get_next_multiple_of_5(from_range):
    for n in range(from_range, from_range + 10):
        if n % 5 == 0:
            return n

def gradingStudents(grades):
    # Write your code here
    result = []
    
    for grade in grades:
        n = get_next_multiple_of_5(grade)
        if n - grade < 3 and grade >= 38:
            result.append(n)
        else:
            result.append(grade)
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
