import sys

M, N = list(map(int, sys.stdin.readline().split()))
index = 1
name_to_idx = dict()
idx_to_name = dict()

for _ in range(M):
    name = sys.stdin.readline().rstrip()
    name_to_idx[name] = index
    idx_to_name[index] = name
    index += 1

for _ in range(N):
    q = sys.stdin.readline().rstrip()
    if q in name_to_idx:
        print(name_to_idx[q])
    else:
        print(idx_to_name[int(q)])
