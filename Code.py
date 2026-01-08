from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    blocks = deque(map(int, input().split()))
    
    top = float('inf')
    
    while blocks:
        if blocks[0] <= top and blocks[-1] <= top:
            # choose the larger one
            if blocks[0] >= blocks[-1]:
                top = blocks.popleft()
            else:
                top = blocks.pop()
        elif blocks[0] <= top:
            top = blocks.popleft()
        elif blocks[-1] <= top:
            top = blocks.pop()
        else:
            print("No")
            break
    else:
        print("Yes")
