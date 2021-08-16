import sys


def dp(idx, length, N, x):
    if length == x:
        return 1
    if length > x:
        return 0
    if idx == N:
        return 0
    ret = dp_[idx][length]
    if ret != -1:
        return ret
    ret = 0
    for num in range(C[idx]):
        ret += dp(idx+1, length+L[idx]*num, N, x)
    return ret
    


N, x = list(map(int, sys.stdin.readline().split()))
L = []
C = []
for _ in range(N):
    a, b = list(map(int, sys.stdin.readline().split()))
    L.append(a)
    C.append(b)
dp_ = [[-1]*10001 for _ in range(100)]
print(dp(0,0,N,x))


