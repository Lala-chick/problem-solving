from collections import deque


def bfs(N, K):
    queue = deque()
    queue.append((N, 0))

    dts = [1, -1, N]
    visited = [0 for _ in range(100001)]

    while queue:
        n, cnt = queue.popleft()
        if n == K:
            return cnt
        visited[n] = 1
        dts[-1] = n
        for dt in dts:
            mn = n + dt
            if 0 <= mn < 100001 and visited[mn] == 0:
                queue.append((mn, cnt + 1))


N, K = list(map(int, input().split()))
answer = bfs(N, K)
print(answer)
