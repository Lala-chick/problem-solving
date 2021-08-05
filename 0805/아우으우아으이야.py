import sys

N = int(sys.stdin.readline().rstrip())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

start, end = lines.pop(0)
answer = 0

for x, y in lines:
    if x <= end:
        end = max(y, end)
    elif x > end:
        answer += (end - start)
        start = x
        end = y

answer += (end - start)

print(answer)