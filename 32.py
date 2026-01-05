from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])  # ignore first number (count)

max_value = 0

for combo in product(*lists):
    value = sum(x*x for x in combo) % M
    max_value = max(max_value, value)

print(max_value)
