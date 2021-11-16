#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus = 0
    minus = 0

    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1

    print(round(plus / len(arr), 6))
    print(round(minus / len(arr), 6))
    print(round((len(arr) - plus - minus) / len(arr), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
