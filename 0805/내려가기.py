import sys

N = int(sys.stdin.readline().rstrip())

min_table = list(map(int, sys.stdin.readline().split()))
max_table = [i for i in min_table]

for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    min_tmp = [0, 0, 0]
    min_tmp[0] = min(min_table[0]+a, min_table[1]+a)
    min_tmp[1] = min(min_table[0]+b, min_table[1]+b, min_table[2]+b)
    min_tmp[2] = min(min_table[1]+c, min_table[2]+c)
    min_table = min_tmp
    max_tmp = [0, 0, 0]
    max_tmp[0] = max(max_table[0]+a, max_table[1]+a)
    max_tmp[1] = max(max_table[0]+b, max_table[1]+b, max_table[2]+b)
    max_tmp[2] = max(max_table[1]+c, max_table[2]+c)
    max_table = max_tmp

print(max(max_table), min(min_table))