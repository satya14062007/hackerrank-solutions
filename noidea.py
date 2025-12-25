# Read n and m (m is not actually needed)
n, m = map(int, input().split())

# Read the array
arr = list(map(int, input().split()))

# Read sets A and B
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Calculate happiness
happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

# Output result
print(happiness)
