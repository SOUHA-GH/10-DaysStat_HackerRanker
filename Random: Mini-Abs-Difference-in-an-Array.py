import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    # Initialize the minimum difference with a large value
    min_diff = float('inf')

    # Sort the array in ascending order
    arr.sort()

    # Iterate over the array and calculate the absolute difference
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])

        # Update the minimum difference if a smaller difference is found
        if diff < min_diff:
            min_diff = diff

    return min_diff

if __name__ == '__main__':
    while True:
        try:
            n = int(input().strip())
            if 2 <= n <= 10 ** 5:
                break
            else:
                continue
        except ValueError:
            continue

    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
