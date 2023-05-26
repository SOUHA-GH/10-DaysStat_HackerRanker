import statistics

def interQuartile(values, freqs):
    # Combine values and freqs into a single list
    data = []
    for value, freq in zip(values, freqs):
        data.extend([value] * freq)

    # Calculate quartiles and absolute difference
    data.sort()  # Sort the data list
    N = len(data)
    mid = N // 2
    
    if N % 2 == 0:
        lower_half = data[:mid]
        upper_half = data[mid:]
    else:
        lower_half = data[:mid]
        upper_half = data[mid+1:]
    
    Q1 = statistics.median(lower_half)
    Q3 = statistics.median(upper_half)
    q = abs(Q3 - Q1)
    Q = format(q, ".1f")  # Format the result to one decimal place
    return Q

if __name__ == '__main__':
    while True:
        try:
            n = int(input().strip())
            if 5 <= n <= 50:
                break
            else:
                continue
        except ValueError:
            continue

    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    res = interQuartile(val, freq)
    print(res)
