import sys

N = int(sys.stdin.readline())
plates = list(map(int, sys.stdin.readline().split()))
plates = sorted(plates)

answer = 1
for i in range(N):
    if answer >= plates[i]:
        answer += plates[i]
    else:
        break

print(answer)