from collections import deque
def bfs(warehouse, visited, queue, N, M):

    ans = 0
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = 1

        for dx, dy in zip(dxs, dys):
            next_x = x + dx
            next_y = y + dy

            if 0 <= next_x < M and 0 <= next_y < N:
                if visited[next_x][next_y] == 0 and warehouse[next_x][next_y] == 0:
                    warehouse[next_x][next_y] = 1
                    queue.append((next_x, next_y, cnt+1))
                    ans = max(ans, cnt+1)
    
    return ans

def print_answer(answer, warehouse):
    for i in range(N):
        for j in range(M):
            if warehouse[i][j] == 0:
                print(-1)
                return
    print(answer)

M, N = list(map(int, input().split()))
warehouse = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
idxs = deque()
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and warehouse[i][j] == 1:
            idxs.append((i, j, 0))

answer = bfs(warehouse, visited, idxs, M, N)
print_answer(answer, warehouse)