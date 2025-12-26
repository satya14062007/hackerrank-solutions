from collections import namedtuple

n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)

total = 0
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)

print(f"{total / n:.2f}")
