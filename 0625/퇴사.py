N = int(input())
T = [0 for _ in range(N)]
P = [0 for _ in range(N)]

for i in range(N):
    T[i], P[i] = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

if T[-1] + N - 1 <= N:
    dp[N-1] = P[-1]

for i in range(N-2, -1, -1):
    if T[i] + i <= N:
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])