import sys
import math

W, L, D = list(map(float, sys.stdin.readline().split()))

fac_20 = math.factorial(20)

tier = [0 for _ in range(5)]

for win in range(0, 21):
    for lose in range(0, 21):
        for draw in range(0, 21):
            if win + lose + draw == 20:
                score = 2000 + win * 50 - lose * 50
                prob = W**win * L**lose * D**draw * (fac_20/(math.factorial(win)*math.factorial(lose)*math.factorial(draw)))

                if 1000 <= score < 1500:
                    tier[0] += prob
                elif 1500 <= score < 2000:
                    tier[1] += prob
                elif 2000 <= score < 2500:
                    tier[2] += prob
                elif 2500 <= score < 3000:
                    tier[3] += prob
                elif 3000 <= score < 3500:
                    tier[4] += prob

for i in range(5):
    tmp = round(tier[i], 8)
    print(format(tmp, '.8f'))