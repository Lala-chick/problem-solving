import sys

N, M, K = list(map(int, sys.stdin.readline().split()))

nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

for _ in range(M+K):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if a == 1:
        nums[b-1] = c
    elif a == 2:
        print(sum(nums[b-1:c]))
