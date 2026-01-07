import re

n = int(input())
pattern = r'^[789]\d{9}$'

for _ in range(n):
    print("YES" if re.match(pattern, input().strip()) else "NO")
