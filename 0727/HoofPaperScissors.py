import sys

def sol(rock, scissors, paper, games):
    player1 = 0
    player2 = 0
    for left, right in games:
        if left == rock:
            if right == scissors:
                player1 += 1
            elif right == paper:
                player2 += 1
        if left == scissors:
            if right == paper:
                player1 += 1
            elif right == rock:
                player2 += 1
        if left == paper:
            if right == rock:
                player1 += 1
            elif right == scissors:
                player2 += 1
    
    return max(player1, player2)


N = int(sys.stdin.readline())
games = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0

for i in range(6):
    if i == 0:
        answer = max(sol(1, 2, 3, games), answer)
    elif i == 1:
        answer = max(sol(1, 3, 2, games), answer)
    elif i == 2:
        answer = max(sol(2, 1, 3, games), answer)
    elif i == 3:
        answer = max(sol(2, 3, 1, games), answer)
    elif i == 4:
        answer = max(sol(3, 1, 2, games), answer)
    elif i == 5:
        answer = max(sol(3, 2, 1, games), answer)

print(answer)