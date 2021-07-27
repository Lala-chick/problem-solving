import sys
import math

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break

    print(math.factorial(2*N)//(math.factorial(N)*math.factorial(N+1)))