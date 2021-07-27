import sys
from collections import deque
import heapq

def find_start(ocean):
    position = None

    for i in range(N):
        for j in range(N):
            if ocean[i][j] == 9:
                position = (i, j)
                ocean[i][j] = 0
                return position, ocean

def eat_fish(ocean, position, N, size):

    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    
    x,y = position
    heap = []

    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y,0))

    while queue:
        x, y, d = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if ocean[nx][ny] == 0 or ocean[nx][ny] == size:
                        queue.append([nx, ny, d+1])
                    elif size > ocean[nx][ny]:
                        heapq.heappush(heap, [d+1, nx, ny])

    if heap:
        return heap[0]
    else:
        return None

def mini_shark(ocean, start, N):

    size = 2
    cnt = 0
    answer = 0

    while True:
        results = eat_fish(ocean, start, N, size)
        if results is None:
            break
        
        answer += results[0]
        cnt += 1
        start = (results[1], results[2])
        ocean[start[0]][start[1]] = 0
        if cnt == size:
            cnt = 0
            size += 1

    return answer


N = int(sys.stdin.readline())
ocean = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

position, ocean = find_start(ocean)
print(mini_shark(ocean, position, N))

