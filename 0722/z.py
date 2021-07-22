import sys

N, r, c = list(map(int, sys.stdin.readline().split()))

answer = 0

while N > 1:
    max_ = (2 ** N) // 2
    if r < max_ and c < max_:
        pass
    elif r < max_ and c >= max_:
        answer += (max_ ** 2)
        c -= max_
    elif r >= max_ and c < max_:
        answer += (max_ ** 2) * 2
        r -= max_
    elif r >= max_ and c >= max_:
        answer += (max_ ** 2) * 3
        r -= max_
        c -= max_
    N -= 1

if r == 0 and c == 0:
    print(answer)
if r == 0 and c == 1:
    print(answer + 1)
if r == 1 and c == 0:
    print(answer + 2)
if r == 1 and c == 1:
    print(answer + 3)