import sys
from itertools import combinations

def calc_distance(result, map_, N, M):
    ret = 5000
    for i in range(len(result)):
        dist = 0
        for x in range(N):
            for y in range(N):
                if map_[x][y] == 1:
                    tmp = 50000
                    for j in range(M):
                        tmp = min(tmp, abs(x-result[i][j][0])+abs(y-result[i][j][1]))
                    dist += tmp
        ret = min(ret, dist)
    return ret

N, M = list(map(int, sys.stdin.readline().split()))
map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chickens = []
for i in range(N):
    for j in range(N):
        if map_[i][j] == 2:
            chickens.append((i, j))
            map_[i][j] = 0

result = list(combinations(chickens, M))
print(calc_distance(result, map_, N, M))