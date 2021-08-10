import sys
import math

def find_height(D, H, a, b, c):
    alpha = math.tan((a/180) * math.pi)
    beta = math.tan((b/180) * math.pi)
    gamma = math.tan((c/180) * math.pi)
    height = math.sqrt(2*(D**2)*(alpha**2)*(beta**2)*(gamma**2)/(((alpha**2)*(beta**2))+((beta**2)*(gamma**2))-(2*(alpha**2)*(gamma**2))))
    height += H

    return round(height)


D, H = list(map(float, sys.stdin.readline().split()))
while True:
    a, b, c = list(map(float, sys.stdin.readline().split()))
    if a <= 0.0:
        break
    print(find_height(int(D), int(H), a, b, c))