import sys

N, M = list(map(int, sys.stdin.readline().split()))

ans = 0
dp = [1]*(N+1)
if N >= M:
    dp[M] = 2

for i in range(M+1, N+1):
    dp[i] = (dp[i-1] + dp[i-M]) % 1000000007

print(dp[N])