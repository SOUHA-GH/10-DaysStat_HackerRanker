from math import comb

def calculate_probability(defective_percentage, batch_size):
    p = defective_percentage / 100  # Convert percentage to decimal
    q = 1 - p  # Probability of a piston not being defective
    probability_no_more_than_2_rejects = sum(comb(batch_size, i) * (p ** i) * (q ** (batch_size - i)) for i in range(3))
    probability_at_least_2_rejects = 1 - (comb(batch_size, 0) * (p ** 0) * (q ** batch_size) + comb(batch_size, 1) * (p ** 1) * (q ** (batch_size - 1)))
    return round(probability_no_more_than_2_rejects, 3), round(probability_at_least_2_rejects, 3)

# Read input values
defective_percentage, batch_size = map(int, input().split())

# Calculate probabilities
result = calculate_probability(defective_percentage, batch_size)

# Print the results
print(result[0])
print(result[1])
