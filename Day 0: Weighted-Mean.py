#!/bin/python3

import math
import os
import random
import re
import sys

def weightedMean(X, W):
    N = len(X)
    sum_X = sum(x * w for x, w in zip(X, W))
    sum_W = sum(W)
    weighted_mean = sum_X / sum_W
    return round(weighted_mean, 1)

if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().rstrip().split()))
    W = list(map(int, input().rstrip().split()))

    result = weightedMean(X, W)
    print(result)
