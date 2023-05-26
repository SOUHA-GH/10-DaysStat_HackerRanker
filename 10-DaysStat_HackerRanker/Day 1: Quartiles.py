#!/bin/python3
import statistics

def quartiles(arr):
    arr.sort()
    N = len(arr)

    Q1 = statistics.median(arr[:N//2])
    Q2 = statistics.median(arr)
    Q3 = statistics.median(arr[(N+1)//2:])

    return [int(Q1), int(Q2), int(Q3)]

if __name__ == '__main__':
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data)
    print('\n'.join(map(str, res)))
