import sys

N, K = list(map(int, sys.stdin.readline().split()))
coins = []
answer = 0

for _ in range(N):
    coin = int(sys.stdin.readline().rstrip())
    if coin <= K:
        coins.append(coin)

for coin in coins[::-1]:
    answer += K // coin
    K %= coin

print(answer)
