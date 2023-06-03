def calculate_probability(num, den, k):
    p = num / den  # Convert probability to decimal
    probability = (1 - p) ** (k - 1) * p
    return round(probability, 3)

# Read input values
numerator, denominator = map(int, input().split())
k = int(input())

# Calculate the probability
result = calculate_probability(numerator, denominator, k)

# Print the result
print(result)
