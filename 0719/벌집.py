import sys

N = int(sys.stdin.readline().rstrip())

tmp = 1
answer = 0
plus = 6

while tmp < N:
    answer += 1
    tmp += (answer*plus)

print(answer+1)