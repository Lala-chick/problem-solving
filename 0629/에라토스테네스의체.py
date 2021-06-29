import sys

def eratos(N, K):

    visited = [0] * (N+1)

    cnt = 0

    for i in range(2, N+1):
        for j in range(i, N+1, i):
            if visited[j] == 0:
                visited[j] = 1
                cnt += 1
                if cnt == K:
                    return j


N, K = list(map(int, sys.stdin.readline().split()))

print(eratos(N, K))