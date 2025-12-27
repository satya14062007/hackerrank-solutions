# Read input
m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

# Find symmetric difference
result = a.symmetric_difference(b)

# Print in ascending order
for value in sorted(result):
    print(value)
