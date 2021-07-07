import sys

N, H = list(map(int, sys.stdin.readline().split()))

stalagmites = [0] * (H+1)
stalactites = [0] * (H+1)

cnt = N
answer = 0

for i in range(N):
    length = int(sys.stdin.readline().rstrip())
    if i % 2 == 0:
        stalagmites[length] += 1
    else:
        stalactites[length] += 1

for i in range(H-1, 1, -1):
    stalagmites[i-1] += stalagmites[i]
    stalactites[i-1] += stalactites[i]


for i in range(1, H+1):
    num_stones = stalagmites[i] + stalactites[H-i+1]
    if cnt > num_stones:
        cnt = num_stones
        answer = 1
    elif cnt == num_stones:
        answer += 1

print(cnt,answer)
    
