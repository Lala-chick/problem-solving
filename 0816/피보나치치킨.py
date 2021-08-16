import sys

N = int(sys.stdin.readline().rstrip())

min_chicken = (N+1)//2
max_chicken = (N*2)//3
print(min_chicken, max_chicken)