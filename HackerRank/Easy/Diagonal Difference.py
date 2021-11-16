#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primaryDiagonal = 0
    secondDiagonal = 0

    primaryList = [i for i in range(len(arr))]
    secondList = [i for i in range(len(arr) - 1, -1, -1)]

    for i in range(len(arr)):
        primaryDiagonal += arr[i][primaryList[i]]
        secondDiagonal += arr[i][secondList[i]]

    return abs(primaryDiagonal - secondDiagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
