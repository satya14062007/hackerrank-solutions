def average(arr):
    distinct_heights = set(arr)
    return round(sum(distinct_heights) / len(distinct_heights), 3)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(average(arr))
