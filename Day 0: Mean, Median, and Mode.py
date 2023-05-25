from collections import Counter 
import statistics
while True:
    try:
        N = int(input(""))
        if 10 <= N <= 2500:
            break
        else:
            continue
    except ValueError:
        continue
input_string = input("")
X = list(map(int, input_string.split()))
N=len(X)
mean = (sum(X)/N)
print(mean)
X.sort()
median = statistics.median(X)
print(median)
def find_mode(array):
    counter = Counter(array)
    max_occurrences = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_occurrences]
    smallest_mode = min(modes)
    return smallest_mode
mode = find_mode(X)
print(mode)
