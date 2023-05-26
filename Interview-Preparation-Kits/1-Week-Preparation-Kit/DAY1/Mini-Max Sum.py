#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    n = len(arr)
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    return min_sum, max_sum
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    res=miniMaxSum(arr)
    output_list = [str(value) for value in res]
    output_string = ' '.join(output_list)
    print(output_string)
