import sys
from collections import deque

def bfs(map_, visited, N):
    queue = deque()
    answer = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)
            answer += 1
            while queue:
                tmp = queue.popleft()
                for j in map_[tmp]:
                    if visited[j] == 0:
                        visited[j] = 1
                        queue.append(j)
    
    print(answer)


N, M = list(map(int, sys.stdin.readline().split()))

map_ = [[]*N for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    map_[u].append(v)
    map_[v].append(u)

bfs(map_, visited, N)