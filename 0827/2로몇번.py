import sys

def solution(x):
    ret = x
    i = 2
    while i <= x:
        ret += (x//i)*(i//2)
        i *= 2
    return ret

A, B = list(map(int, sys.stdin.readline().split()))
print(solution(B)-solution(A-1))
