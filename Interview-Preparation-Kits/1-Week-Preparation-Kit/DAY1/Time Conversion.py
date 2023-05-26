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
    # Write your code here
    # Separate hours, minutes, and seconds from the input time
    hours, minutes, seconds_period = map(int, s[:-2].split(':'))
    period = s[-2:]  # AM or PM

    # Perform conversion
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0

    # Format the result in 24-hour format
    result = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds_period)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
