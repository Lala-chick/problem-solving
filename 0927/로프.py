import sys

answer = 0
N = int(sys.stdin.readline().rstrip())
ropes = []
for _ in range(N):
    ropes.append(int(sys.stdin.readline().rstrip()))

ropes.sort(reverse=True)
for i, rope in enumerate(ropes):
    tmp = rope * (i+1)
    answer = max(tmp, answer)

print(answer)