from itertools import permutations

# Input
s, k = input().split()
k = int(k)

# Sort the string
s = sorted(s)

# Generate and print permutations
for p in permutations(s, k):
    print("".join(p))
