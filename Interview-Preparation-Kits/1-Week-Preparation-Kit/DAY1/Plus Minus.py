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
    n=len(arr)
    arr.sort()
    p=0
    neg=0
    z=0
    for i in range(n):
        if (arr[i]>0):
            p+=1
        elif (arr[i]<0):
            neg+=1
        else:
            z+=1
    parr = format(p/n, ".6f")
    narr = format(neg/n, ".6f")
    zarr = format(z/n, ".6f")
    return (parr,  narr,zarr)
if __name__ == '__main__':
    while True:
        try:
            n = int(input().strip())
            if 0 <= n <= 100:
                break
            else:
                continue
        except ValueError:
            continue
    arr = list(map(int, input().rstrip().split()))
    res=plusMinus(arr)
    for val in res:
        print(val)
