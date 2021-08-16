import sys

def roll_cake(zero, non_zero, M):
    ans = 0

    for z in zero:
        while z > 10:
            z -= 10
            ans += 1
            M -= 1
            if M == 0:
                if z == 10:
                    return ans + 1
                return ans
        if z == 10:
            ans += 1
    
    for nz in non_zero:
        while nz >= 10:
            nz -= 10
            ans += 1
            M -= 1
            if M == 0:
                return ans
    
    return ans

N, M = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

ans = 0
zero = []
non_zero = []

for a in A:
    if a == 10:
        ans += 1
    elif a % 10 == 0:
        zero.append(a)
    elif a % 10 != 0 and a > 10:
        non_zero.append(a)

if not zero and not non_zero:
    print(ans)

else:
    zero.sort()
    non_zero.sort()

    print(ans+roll_cake(zero, non_zero, M))

