#!/bin/python

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    result = "{}.09.{}".format("12" if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0) or (year <= 1917 and year % 4 == 0) else "13", year)
    return "26.09.1918" if year == 1918 else result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(raw_input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
