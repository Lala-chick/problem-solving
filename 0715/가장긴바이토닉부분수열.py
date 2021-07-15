import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A_rev = A[::-1]
dp = [0] * N
dp_rev = [0] * N

for i in range(N):
    for j in range(i):
        if A[i]>A[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

for i in range(N):
    for j in range(i):
        if A_rev[i]>A_rev[j] and dp_rev[i]<dp_rev[j]:
            dp_rev[i] = dp_rev[j]
    dp_rev[i] += 1

dp_rev = dp_rev[::-1]

answer = 0

for cnt, cnt_rev in zip(dp, dp_rev):
    answer = max(answer, cnt+cnt_rev-1)
print(answer)