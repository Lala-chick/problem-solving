N = int(input())
P = list(map(int, input().split()))
P.sort()
withdraw_times = 0
answer = 0

for time in P:
    withdraw_times += time
    answer += withdraw_times

print(answer)