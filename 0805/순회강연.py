import sys
import heapq

N = int(sys.stdin.readline().rstrip())
pd = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

pd = sorted(pd, key=lambda x:(x[1], -x[0]))
heap = []
for p, d in pd:
    heapq.heappush(heap, (p, d))
    if len(heap) > d:
        while len(heap) > d:
            heapq.heappop(heap)
print(heap)
answer = 0

for p, _ in heap:
    answer += p
print(answer)