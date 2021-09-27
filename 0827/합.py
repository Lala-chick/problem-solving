import sys

def summation(x):
    if x <= 0:
        return 0
    s = [0] * 10
    ret = 0
    point = 1
    while x > 0:
        while x % 10 != 9:
            for i in str(x):
                s[int(i)] += point
            x -= 1
        if x < 10:
            for i in range(x+1):
                s[i] += point
            break
        else:
            for i in range(10):
                s[i] += (x//10 + 1) * point
        point *= 10
        x //= 10
    for i in range(10):
        ret += i*s[i]
    return ret

L, U = list(map(int, sys.stdin.readline().split()))

ans = summation(U) - summation(L-1)

print(ans)
