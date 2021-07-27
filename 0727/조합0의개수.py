import sys
import math

def combi(n, div):
    ret = 0
    count = 1
    while n // (div**count) > 0:
        ret += n // (div**count)
        count += 1
    return ret

n, m = list(map(int, sys.stdin.readline().split()))

cnt5 = combi(n, 5) - combi(n-m, 5) - combi(m, 5)
cnt2 = combi(n, 2) - combi(n-m, 2) - combi(m, 2)

print(min(cnt5, cnt2))