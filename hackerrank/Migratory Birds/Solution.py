#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    numberDict = collections.defaultdict(int)
    result = 0
    times = 0
    for number in arr:
        numberDict[number] += 1
        if numberDict[number] > times:
            result = number
            times = numberDict[number]
        elif numberDict[number] == times and result > number:
            result = number
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
