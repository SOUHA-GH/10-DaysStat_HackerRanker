#!/bin/python3

import math

def stdDev(arr):
    arr.sort()
    N = len(arr)
    s = sum(arr)
    m = int(s / N)
    std = 0  # Initialize std to 0
    for i in range(N):
        std += math.pow(int(arr[i] - m), 2) 
    stddiv = math.sqrt(std / N)
    return (round(stddiv, 1))

if __name__ == '__main__':
    while True:
        try:
            n = int(input().strip())
            if 5 <= n <= 100:
                break
            else:
                continue
        except ValueError:
            continue
    vals = list(map(int, input().rstrip().split()))
    result = stdDev(vals)
    print(result)
