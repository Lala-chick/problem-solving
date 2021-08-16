import sys

x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(x1, x2):
    if i%2 == 1:
        answer += min(y2, i) - min(y1, i)

for i in range(y1, y2):
    if i % 2 == 1:
        answer += min(x2, i) - min(x1, i)

for i in range(max(x1,y1), min(x2, y2)):
    if i % 2 == 1:
        answer += 1

print(answer)