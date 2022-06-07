import sys
import math

def wave(T, positions, velocities):

    min_ = 0
    max_ = math.inf

    for position, velocity in zip(positions, velocities):
        left = round(position - velocity * T, 4)
        right = round(position + velocity * T, 4)
        
        if (max_ < left) or (right < min_):
            return 0
        
        min_ = max(left, min_)
        max_ = min(right, max_)

    return 1

N, T = list(map(float, sys.stdin.readline().split()))
positions = list(map(float, sys.stdin.readline().split()))
velocities = list(map(float, sys.stdin.readline().split()))

print(wave(T, positions, velocities))