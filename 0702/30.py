import sys

N = list(sys.stdin.readline().rstrip())

N = sorted(N, reverse=True)
sum_ = 0
if '0' not in N:
    print(-1)
else:
    for n in N:
        sum_ += int(n)
    if sum_ % 3 != 0:
        print(-1)
    else:
        print("".join(N))

