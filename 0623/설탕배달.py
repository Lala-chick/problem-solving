def calc_bags(N):
    bags = 0
    while N > 0:
        if N % 5 == 0:
            return bags + N // 5
        bags += 1
        N -= 3
    if N == 0:
        return bags
    else:
        return -1

N = int(input())
answer = calc_bags(N)
print(answer)
