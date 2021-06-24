from collections import deque
def bfs(land, visited, x, y, M, N):
    
    queue = deque()
    queue.append((x,y))
    visited[y][x] = 1
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            mx = x + dx
            my = y + dy
            if 0 <= mx < M and 0 <= my < N:
                if visited[my][mx] == 0 and land[my][mx] == 1:
                    visited[my][mx] = 1
                    queue.append((mx, my)) 
    return

T = int(input())
answers = []
for _ in range(T):
    M, N, K = list(map(int, input().split()))

    land = [[0]*M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        i, j = list(map(int, input().split()))
        land[j][i] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(land, visited, j, i, M, N)
                cnt += 1 

    answers.append(cnt)

for answer in answers:
    print(answer) 