from itertools import combinations_with_replacement

# Read input
s, k = input().split()
k = int(k)

# Sort string
s = sorted(s)

# Generate combinations with replacement
for comb in combinations_with_replacement(s, k):
    print("".join(comb))
