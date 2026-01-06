s = input().strip()

print(
    ''.join(sorted([c for c in s if c.islower()])) +
    ''.join(sorted([c for c in s if c.isupper()])) +
    ''.join(sorted([c for c in s if c.isdigit() and int(c) % 2 == 1])) +
    ''.join(sorted([c for c in s if c.isdigit() and int(c) % 2 == 0]))
)
