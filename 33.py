n, m = map(int, input().split())

rows = []
for _ in range(n):
    rows.append(list(map(int, input().split())))

k = int(input())

rows.sort(key=lambda x: x[k])

for row in rows:
    print(*row)
