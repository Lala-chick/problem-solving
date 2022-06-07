import sys

A, B = list(map(int, sys.stdin.readline().split()))
ans = 1

while True:
    if B == A:
        break
    elif B % 2 != 0 and B % 10 != 1:
        ans = -1
        break
    elif B < A:
        ans = -1
        break
    else:
        if B % 2 == 0:
            B //= 2
        else:
            B //= 10
        ans += 1
print(ans)