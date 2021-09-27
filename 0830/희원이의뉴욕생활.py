import sys
import math

def cross(x, y, bx, by, p, q, r):
    y_ = -p*x/q + (r/q)
    x_ = -q*y/p + (r/p)
    if (x <= x_ <= bx or bx <= x_ <= x):
        return (x_, y)
    elif (y <= y_ <= by or by <= y_ <= y):
        return (x, y_)
    return None

def calc_distance(ax, ay, bx, by, cp1, cp2):
    if cp1 == None or cp2 == None:
        return abs(ax-bx) + abs(ay-by)
    elif cp1[0] == cp2[0] or cp1[1] == cp2[1]:
        return abs(ax-bx) + abs(ay-by)
        
    if ax == bx and ay == by:
        return 0
    elif ax == bx:
        return abs(ay - by)
    elif ay == by:
        return abs(ax - bx)

    if (ax-bx)/(ay-by) > 0 and (cp1[0] - cp2[0])/(cp1[1] - cp2[1]) < 0:
        return abs(ax-bx) + abs(ay-by)
    elif (ax-bx)/(ay-by) < 0 and (cp1[0] - cp2[0])/(cp1[1] - cp2[1]) > 0:
        return abs(ax-bx) + abs(ay-by)

    cross_dist = math.sqrt((cp1[0]-cp2[0])**2 + (cp1[1]-cp2[1])**2)
    dist = 0
    if cp1[0] == ax:
        dist += abs(cp1[1] - ay)
    else:
        dist += abs(cp1[0] - ax)
    if cp2[0] == bx:
        dist += abs(cp2[1] - by)
    else:
        dist += abs(cp2[0] - bx)
    return dist + cross_dist

ax, ay, bx, by, p, q, r = list(map(float, sys.stdin.readline().split()))

cp1 = cross(ax, ay, bx, by, p, q, r)
cp2 = cross(bx, by, ax, ay, p, q, r)
print(f"{calc_distance(ax, ay, bx, by, cp1, cp2):.12f}")