import sys

N, M = list(map(int, sys.stdin.readline().split()))
meats = []
for _ in range(N):
    i, j = list(map(int, sys.stdin.readline().split()))
    meats.append((i,j))

meats = sorted(meats, key=lambda x:(x[1], -x[0]))

weights = 0
prices = 0
for weight, price in meats:
    weights += weight

    if weights >= M:
        weights += weight
        prices = price
        break
    weights += weight
    prices = price

if weights < M:
    print(-1)
else:
    print(prices)