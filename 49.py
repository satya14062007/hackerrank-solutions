n, m = map(int, input().split())

marks = []
for _ in range(m):
    marks.append(list(map(float, input().split())))

# Transpose and calculate averages
for student_marks in zip(*marks):
    avg = sum(student_marks) / m
    print(avg)
