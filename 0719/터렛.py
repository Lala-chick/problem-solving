import sys


def calc_dist(x1, y1, r1, x2, y2, r2):
    dist = int((x1-x2)**2 + (y1-y2)**2)
    dist_r = (r1+r2) ** 2
    dist_r_sub = (r1-r2) ** 2

    if dist == 0:
        if r1 == r2:
            return -1
        elif r1 != r2:
            return 0
    if dist > dist_r:
        return 0
    elif dist == dist_r:
        return 1
    else:
        if dist_r_sub == dist:
            return 1
        elif dist_r_sub > dist:
            return 0
        else:
            return 2


T = int(sys.stdin.readline().rstrip())
turrets = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for x1, y1, r1, x2, y2, r2 in turrets:
    print(calc_dist(x1, y1, r1, x2, y2, r2))