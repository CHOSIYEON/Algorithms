#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s[8:]

    if time == 'PM':
        if int(s[0:2]) < 12:
            return str(int(s[0:2]) + 12) + s[2:8]
    else:
        if int(s[0:2]) >= 12 and int(s[0:2]) < 22:
            return ('0' + str(int(s[0:2]) - 12) + s[2:8])
        elif int(s[0:2]) >= 22:
            return (str(int(s[0:2]) - 12) + s[2:8])

    return s[:8]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
