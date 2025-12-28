from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    name, price = input().rsplit(' ', 1)
    price = int(price)

    if name in items:
        items[name] += price
    else:
        items[name] = price

for item, net_price in items.items():
    print(item, net_price)
