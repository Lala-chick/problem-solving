import sys
from collections import deque

def bfs(A, B, C):
    total = A+B+C
    visited = [[0]*(total) for _ in range(total)]
    queue = deque()
    queue.append((A, B))
    visited[A][B] = 1

    while queue:
        a, b = queue.popleft()
        c = total - (a + b)
        if a == b == c:
            return 1
        for x, y in [(a, b), (b, c), (a, c)]:
            if x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            else:
                continue
            z = total - (x+y)
            a = min(x, y, z)
            b = max(x, y, z)
            if not visited[a][b]:
                visited[a][b] = 1
                queue.append((a,b))
    return 0 


A, B, C = map(int, sys.stdin.readline().split())

if (A+B+C) % 3 != 0:
    print(0)
else:
    print(bfs(A, B, C))
