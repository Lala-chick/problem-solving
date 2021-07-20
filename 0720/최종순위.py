import sys

n, p, k, d = list(map(int, sys.stdin.readline().split()))

d -= 1

if d != 0:
    best = p - d * (d-1) // 2
    if best <= d:
        print("Wrong information")
    else:
        print(best)
        for i in range(1, d):
            print(d-i)
        for i in range(d, n):
            print(0)

elif p % k == 0:
    for i in range(k):
        print(p//k)
    for i in range(k,n):
        print(0)

elif k < n and p // k * (n-k) >= p%k:
    f = p//k
    for i in range(k):
        print(f)
        p -= f
    for i in range(k, n):
        s = min(f, p)
        print(s)
        p -= s
else:
    print("Wrong information")