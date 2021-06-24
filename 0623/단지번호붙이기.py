from collections import deque

def bfs(lst, visited, y, x, N):
    
    nums = 1
    visited[y][x] = 1
    queue = deque()
    queue.append((x, y))

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < N and 0 <= next_y < N:
                if lst[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                    visited[next_y][next_x] = 1 
                    queue.append((next_x, next_y))
                    nums += 1

    return nums

N = int(input())

lst = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1 and visited[i][j] == 0:
            answer.append(bfs(lst, visited, i ,j, N))

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)