n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

# Union of both sets
total_students = english.union(french)

print(len(total_students))

