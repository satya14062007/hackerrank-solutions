from datetime import datetime

t = int(input())

for _ in range(t):
    t1 = input()
    t2 = input()

    dt1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    diff = abs(int((dt1 - dt2).total_seconds()))
    print(diff)
