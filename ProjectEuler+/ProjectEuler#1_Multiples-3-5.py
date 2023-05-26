#!/bin/python3

import sys

total_sum = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total_sum = 0  # Reset the sum for each test case
    for j in range(1, n):
        if j % 3 == 0 or j % 5 == 0:
            total_sum += j
    print(total_sum)
