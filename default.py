from collections import defaultdict

# Read n and m
n, m = map(int, input().split())

# Create defaultdict of list
positions = defaultdict(list)

# Read group A words
for i in range(1, n + 1):
    word = input().strip()
    positions[word].append(i)

# Read group B words and print results
for _ in range(m):
    word = input().strip()
    if word in positions:
        print(" ".join(map(str, positions[word])))
    else:
        print(-1)
