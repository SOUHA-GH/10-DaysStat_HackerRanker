import math

mean_A, mean_B = map(float, input().split())
cost_of_operating_A = 160 + (40 * (math.pow(mean_A, 2) + mean_A))
cost_of_operating_B = 128 + (40 * (math.pow(mean_B, 2) + mean_B))
print(round(cost_of_operating_A, 3))
print(round(cost_of_operating_B, 3))
