n = int(input())
word_count = {}

for _ in range(n):
    word = input().strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Output
print(len(word_count))
print(*word_count.values())
