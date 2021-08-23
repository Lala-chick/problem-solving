import sys
import math
from collections import defaultdict

V, E = list(map(int, sys.stdin.readline().split()))
edge = defaultdict(list)

for i in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    edge[u].append([v,w])
    edge[v].append([u,w])

yak = list(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline().rstrip())

yogurt = yak[0]
dist = 0
for i in range(10):
    cur_dist = dij(dist, yak[i])
    if cur_dist == math.inf:
        continue
    dist += cur_dist
    dist