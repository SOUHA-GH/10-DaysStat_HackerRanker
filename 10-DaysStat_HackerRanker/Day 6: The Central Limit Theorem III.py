import math

sample_size = int(input())
mean_pop = float(input())
std_dev = float(input())
dist_perc = float(input())
z = float(input())

A = mean_pop - z*std_dev/math.sqrt(sample_size)
B = mean_pop + z*std_dev/math.sqrt(sample_size)

print(round(A, 2))
print(round(B, 2))
