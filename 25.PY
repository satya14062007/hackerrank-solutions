from collections import Counter

# Read input
num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_customers = int(input())

# Initialize earnings
earnings = 0

# Process customers
for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1

# Print earnings
print(earnings)